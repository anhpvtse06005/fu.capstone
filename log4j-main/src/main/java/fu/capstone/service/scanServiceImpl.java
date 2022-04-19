package fu.capstone.service;

import org.apache.commons.io.IOUtils;
import org.springframework.stereotype.Service;
import org.springframework.util.ResourceUtils;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class scanServiceImpl implements scanService {
    @Override
    public boolean scan(String web) throws Exception {
        ProcessBuilder processBuilder =  new ProcessBuilder("python", resolvePythonScriptPath("log4j-scan.py"),"-u",web);
//        processBuilder.redirectErrorStream(true);

        Process process = processBuilder.start();
        System.out.println(processBuilder.command().toString());
        boolean check = false;

        List<String> running = readProcessOutput(process.getInputStream());
        for(String string : running){
            System.out.println(string);
        }
        List<String> vulnerable = running.stream().filter(x -> x.contains("Targets do not seem to be vulnerable")).collect(Collectors.toList());
        if(vulnerable.size() ==1){
           check = false;
        }
        List<String> affected = running.stream().filter(x -> x.contains("Targets Affected")).collect(Collectors.toList());
        if(affected.size() == 1){
           check = true;
        }
        return check;
    }

    public static void main(String[] args) throws IOException, InterruptedException {
        ProcessBuilder processBuilder = new ProcessBuilder("python",resolvePythonScriptPath("log4j-scan.py"),"-u http://60a0-58-186-52-181.ngrok.io/api/test/testAccess");
//        ProcessBuilder processBuilder = new ProcessBuilder("pip3", "install","-r",resolvePythonScriptPath("requirements.txt"));
//        ProcessBuilder processBuilder = new ProcessBuilder("python3", resolvePythonScriptPath("log4j-scan.py"),"-u","http://60a0-58-186-52-181.ngrok.io/api/test/testAccess");

//        processBuilder.redirectErrorStream(true);


        Process process = processBuilder.start();
        List<String> running = readProcessOutput(process.getInputStream());
        List<String> vulnerable = running.stream().filter(x -> x.contains("Targets do not seem to be vulnerable")).collect(Collectors.toList());
        if(vulnerable.size() ==1){
            System.out.println("THING");
        }
        List<String> affected = running.stream().filter(x -> x.contains("Targets Affected")).collect(Collectors.toList());
        if(affected.size() == 1){
            System.out.println("Target Affected");
        }
        for(String string : running){
            System.out.println(string);
        }
        int exitCode = process.waitFor();
        System.out.println(exitCode);
        System.out.println("-------------------------------------------------");

    }

    private static String resolvePythonScriptPath(String filename) throws FileNotFoundException {
        File resouse = ResourceUtils.getFile("classpath:python/"+filename);
//        File resouse = new File("src/main/resources/python" + filename);
        return resouse.getAbsolutePath();
    }
    private static List<String> readProcessOutput(InputStream inputStream) throws IOException {
        return IOUtils.readLines(inputStream, "UTF-8");
    }
}
