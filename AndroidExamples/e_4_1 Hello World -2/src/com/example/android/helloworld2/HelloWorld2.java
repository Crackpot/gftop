package com.example.android.helloworld2;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;

/** ����HelloWorldӦ�ó��� **/
public class HelloWorld2 extends Activity {
	OnClickListener listener1 = null;

	/** Called when the activity is first created. */
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		/** ��Button01�����ʱ����������listener1�Ĵ������ **/
		listener1 = new OnClickListener() {
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				/** ����ʾ����ģ����ȡ��TextView01������TextView�࣬ʵ��������text_view **/
				TextView text_view = (TextView) findViewById(R.id.TextView01);
				/** �����ַ����б���text_view_old������ɵ���Ϣ **/
				CharSequence text_view_old = text_view.getText();
				/** �����µ���Ϣ������TextView01����ʾ���� **/
				text_view.setText("�޸�ǰ��" + text_view_old + "\n"
						+ "�����µ���Ϣ��Hello World again!");
			}
		};
		/** ��ʾmain.XML���� **/
		setContentView(R.layout.main);
		Button button1 = (Button) findViewById(R.id.Button01);
		button1.setOnClickListener(listener1);
	}
}