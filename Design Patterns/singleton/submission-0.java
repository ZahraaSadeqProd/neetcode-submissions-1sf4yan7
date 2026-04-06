static class Singleton {
    private static volatile Singleton instance = null;
    private String valueString = null;

    private Singleton() {
    }

    public static Singleton getInstance() {
        if (instance == null){
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }

            }
        }
        return instance;
    }

    public String getValue() {
        return valueString;
    }

    public void setValue(String value) {
        valueString = value;
    }
    
}
