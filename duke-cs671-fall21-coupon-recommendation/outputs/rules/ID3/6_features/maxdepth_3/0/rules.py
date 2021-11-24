def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.9848, "depth": 1}
	if obj[1]>1:
		# {"feature": "Distance", "instances": 5889, "metric_value": 0.9535, "depth": 2}
		if obj[5]<=2:
			# {"feature": "Passanger", "instances": 5308, "metric_value": 0.9386, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Education", "instances": 3482, "metric_value": 0.9606, "depth": 4}
				if obj[2]>1:
					# {"feature": "Restaurant20to50", "instances": 1973, "metric_value": 0.9718, "depth": 5}
					if obj[4]<=3.0:
						# {"feature": "Occupation", "instances": 1928, "metric_value": 0.973, "depth": 6}
						if obj[3]>0:
							return 'True'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					elif obj[4]>3.0:
						# {"feature": "Occupation", "instances": 45, "metric_value": 0.8945, "depth": 6}
						if obj[3]<=12:
							return 'True'
						elif obj[3]>12:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]<=1:
					# {"feature": "Restaurant20to50", "instances": 1509, "metric_value": 0.9431, "depth": 5}
					if obj[4]<=2.0:
						# {"feature": "Occupation", "instances": 1408, "metric_value": 0.9512, "depth": 6}
						if obj[3]<=19.084459450661505:
							return 'True'
						elif obj[3]>19.084459450661505:
							return 'True'
						else: return 'True'
					elif obj[4]>2.0:
						# {"feature": "Occupation", "instances": 101, "metric_value": 0.7562, "depth": 6}
						if obj[3]<=18:
							return 'True'
						elif obj[3]>18:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Restaurant20to50", "instances": 1826, "metric_value": 0.8821, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Occupation", "instances": 1233, "metric_value": 0.9021, "depth": 5}
					if obj[3]<=18.642611393170856:
						# {"feature": "Education", "instances": 1131, "metric_value": 0.9129, "depth": 6}
						if obj[2]<=3:
							return 'True'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					elif obj[3]>18.642611393170856:
						# {"feature": "Education", "instances": 102, "metric_value": 0.7335, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>1.0:
					# {"feature": "Occupation", "instances": 593, "metric_value": 0.8338, "depth": 5}
					if obj[3]<=23.84199971430326:
						# {"feature": "Education", "instances": 588, "metric_value": 0.8371, "depth": 6}
						if obj[2]>1:
							return 'True'
						elif obj[2]<=1:
							return 'True'
						else: return 'True'
					elif obj[3]>23.84199971430326:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[5]>2:
			# {"feature": "Passanger", "instances": 581, "metric_value": 0.9944, "depth": 3}
			if obj[0]>0:
				# {"feature": "Education", "instances": 561, "metric_value": 0.9903, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Occupation", "instances": 513, "metric_value": 0.9845, "depth": 5}
					if obj[3]<=7.711500974658869:
						# {"feature": "Restaurant20to50", "instances": 324, "metric_value": 0.9953, "depth": 6}
						if obj[4]>-1.0:
							return 'False'
						elif obj[4]<=-1.0:
							return 'False'
						else: return 'False'
					elif obj[3]>7.711500974658869:
						# {"feature": "Restaurant20to50", "instances": 189, "metric_value": 0.951, "depth": 6}
						if obj[4]>-1.0:
							return 'False'
						elif obj[4]<=-1.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]>3:
					# {"feature": "Occupation", "instances": 48, "metric_value": 0.9685, "depth": 5}
					if obj[3]<=11:
						# {"feature": "Restaurant20to50", "instances": 40, "metric_value": 0.9928, "depth": 6}
						if obj[4]<=3.0:
							return 'True'
						elif obj[4]>3.0:
							return 'False'
						else: return 'False'
					elif obj[3]>11:
						# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[4]<=1.0:
							return 'True'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]<=0:
				# {"feature": "Occupation", "instances": 20, "metric_value": 0.6098, "depth": 4}
				if obj[3]>1:
					# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.3534, "depth": 5}
					if obj[4]<=1.0:
						return 'True'
					elif obj[4]>1.0:
						# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]<=1:
					# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2]>0:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=1.0:
							return 'False'
						elif obj[4]>1.0:
							return 'False'
						else: return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Restaurant20to50", "instances": 2258, "metric_value": 0.9865, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Occupation", "instances": 1494, "metric_value": 0.9605, "depth": 3}
			if obj[3]>1.943768255746133:
				# {"feature": "Education", "instances": 1245, "metric_value": 0.9723, "depth": 4}
				if obj[2]>0:
					# {"feature": "Passanger", "instances": 810, "metric_value": 0.951, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Distance", "instances": 693, "metric_value": 0.9346, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'False'
						else: return 'False'
					elif obj[0]>2:
						# {"feature": "Distance", "instances": 117, "metric_value": 0.9995, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]<=0:
					# {"feature": "Passanger", "instances": 435, "metric_value": 0.9958, "depth": 5}
					if obj[0]>0:
						# {"feature": "Distance", "instances": 376, "metric_value": 0.9901, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						# {"feature": "Distance", "instances": 59, "metric_value": 0.9748, "depth": 6}
						if obj[5]<=2:
							return 'True'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]<=1.943768255746133:
				# {"feature": "Education", "instances": 249, "metric_value": 0.8676, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Distance", "instances": 229, "metric_value": 0.8362, "depth": 5}
					if obj[5]>1:
						# {"feature": "Passanger", "instances": 150, "metric_value": 0.795, "depth": 6}
						if obj[0]<=2:
							return 'False'
						elif obj[0]>2:
							return 'False'
						else: return 'False'
					elif obj[5]<=1:
						# {"feature": "Passanger", "instances": 79, "metric_value": 0.9005, "depth": 6}
						if obj[0]<=2:
							return 'False'
						elif obj[0]>2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]>3:
					# {"feature": "Passanger", "instances": 20, "metric_value": 0.9928, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Distance", "instances": 18, "metric_value": 1.0, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]>1.0:
			# {"feature": "Occupation", "instances": 764, "metric_value": 0.998, "depth": 3}
			if obj[3]<=13.710484759667237:
				# {"feature": "Distance", "instances": 649, "metric_value": 1.0, "depth": 4}
				if obj[5]>1:
					# {"feature": "Passanger", "instances": 414, "metric_value": 0.9926, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Education", "instances": 331, "metric_value": 0.977, "depth": 6}
						if obj[2]<=3:
							return 'False'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					elif obj[0]>2:
						# {"feature": "Education", "instances": 83, "metric_value": 0.9695, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[5]<=1:
					# {"feature": "Passanger", "instances": 235, "metric_value": 0.9757, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Education", "instances": 223, "metric_value": 0.98, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[0]>2:
						# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[2]<=2:
							return 'True'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[3]>13.710484759667237:
				# {"feature": "Passanger", "instances": 115, "metric_value": 0.9154, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Education", "instances": 103, "metric_value": 0.9336, "depth": 5}
					if obj[2]>0:
						# {"feature": "Distance", "instances": 59, "metric_value": 0.9647, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[2]<=0:
						# {"feature": "Distance", "instances": 44, "metric_value": 0.8757, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[2]>0:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[5]<=2:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
