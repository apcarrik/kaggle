def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.9848, "depth": 1}
	if obj[1]>1:
		# {"feature": "Distance", "instances": 5889, "metric_value": 0.9535, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Passanger", "instances": 5308, "metric_value": 0.9386, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Education", "instances": 3482, "metric_value": 0.9606, "depth": 4}
				if obj[2]>1:
					# {"feature": "Restaurant20to50", "instances": 1973, "metric_value": 0.9718, "depth": 5}
					if obj[4]<=3.0:
						# {"feature": "Occupation", "instances": 1928, "metric_value": 0.973, "depth": 6}
						if obj[3]>0:
							# {"feature": "Direction_same", "instances": 1922, "metric_value": 0.9734, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]>3.0:
						# {"feature": "Occupation", "instances": 45, "metric_value": 0.8945, "depth": 6}
						if obj[3]<=12:
							# {"feature": "Direction_same", "instances": 42, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[3]>12:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]<=1:
					# {"feature": "Restaurant20to50", "instances": 1509, "metric_value": 0.9431, "depth": 5}
					if obj[4]<=2.0:
						# {"feature": "Occupation", "instances": 1408, "metric_value": 0.9512, "depth": 6}
						if obj[3]<=19.084459450661505:
							# {"feature": "Direction_same", "instances": 1315, "metric_value": 0.9566, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[3]>19.084459450661505:
							# {"feature": "Direction_same", "instances": 93, "metric_value": 0.8398, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]>2.0:
						# {"feature": "Occupation", "instances": 101, "metric_value": 0.7562, "depth": 6}
						if obj[3]<=18:
							# {"feature": "Direction_same", "instances": 93, "metric_value": 0.7893, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
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
							# {"feature": "Direction_same", "instances": 1053, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[2]>3:
							# {"feature": "Direction_same", "instances": 78, "metric_value": 0.8213, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]>18.642611393170856:
						# {"feature": "Education", "instances": 102, "metric_value": 0.7335, "depth": 6}
						if obj[2]>0:
							# {"feature": "Direction_same", "instances": 73, "metric_value": 0.783, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							# {"feature": "Direction_same", "instances": 29, "metric_value": 0.5788, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>1.0:
					# {"feature": "Occupation", "instances": 593, "metric_value": 0.8338, "depth": 5}
					if obj[3]<=23.84199971430326:
						# {"feature": "Education", "instances": 588, "metric_value": 0.8371, "depth": 6}
						if obj[2]>1:
							# {"feature": "Direction_same", "instances": 358, "metric_value": 0.8657, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[2]<=1:
							# {"feature": "Direction_same", "instances": 230, "metric_value": 0.7863, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]>23.84199971430326:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[6]>2:
			# {"feature": "Passanger", "instances": 581, "metric_value": 0.9944, "depth": 3}
			if obj[0]>0:
				# {"feature": "Education", "instances": 561, "metric_value": 0.9903, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Occupation", "instances": 513, "metric_value": 0.9845, "depth": 5}
					if obj[3]<=7.711500974658869:
						# {"feature": "Restaurant20to50", "instances": 324, "metric_value": 0.9953, "depth": 6}
						if obj[4]>-1.0:
							# {"feature": "Direction_same", "instances": 323, "metric_value": 0.9957, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[4]<=-1.0:
							return 'False'
						else: return 'False'
					elif obj[3]>7.711500974658869:
						# {"feature": "Restaurant20to50", "instances": 189, "metric_value": 0.951, "depth": 6}
						if obj[4]>-1.0:
							# {"feature": "Direction_same", "instances": 187, "metric_value": 0.9539, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[4]<=-1.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]>3:
					# {"feature": "Occupation", "instances": 48, "metric_value": 0.9685, "depth": 5}
					if obj[3]<=11:
						# {"feature": "Restaurant20to50", "instances": 40, "metric_value": 0.9928, "depth": 6}
						if obj[4]<=3.0:
							# {"feature": "Direction_same", "instances": 37, "metric_value": 0.974, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[4]>3.0:
							return 'False'
						else: return 'False'
					elif obj[3]>11:
						# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[4]<=1.0:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
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
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]<=1:
					# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2]>0:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=1.0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
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
						# {"feature": "Direction_same", "instances": 693, "metric_value": 0.9346, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 537, "metric_value": 0.9183, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							# {"feature": "Distance", "instances": 156, "metric_value": 0.9766, "depth": 7}
							if obj[6]<=1:
								return 'False'
							elif obj[6]>1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[0]>2:
						# {"feature": "Distance", "instances": 117, "metric_value": 0.9995, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 95, "metric_value": 0.998, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 22, "metric_value": 0.994, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]<=0:
					# {"feature": "Passanger", "instances": 435, "metric_value": 0.9958, "depth": 5}
					if obj[0]>0:
						# {"feature": "Direction_same", "instances": 376, "metric_value": 0.9901, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 294, "metric_value": 0.979, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							# {"feature": "Distance", "instances": 82, "metric_value": 0.9961, "depth": 7}
							if obj[6]<=1:
								return 'True'
							elif obj[6]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[0]<=0:
						# {"feature": "Distance", "instances": 59, "metric_value": 0.9748, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Direction_same", "instances": 54, "metric_value": 0.9751, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]>2:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]<=1.943768255746133:
				# {"feature": "Education", "instances": 249, "metric_value": 0.8676, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Direction_same", "instances": 229, "metric_value": 0.8362, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Passanger", "instances": 178, "metric_value": 0.7786, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Distance", "instances": 140, "metric_value": 0.7219, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[0]>2:
							# {"feature": "Distance", "instances": 38, "metric_value": 0.9268, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[5]>0:
						# {"feature": "Passanger", "instances": 51, "metric_value": 0.9662, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Distance", "instances": 48, "metric_value": 0.9544, "depth": 7}
							if obj[6]<=1:
								return 'False'
							elif obj[6]>1:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=2:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]>3:
					# {"feature": "Passanger", "instances": 20, "metric_value": 0.9928, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Distance", "instances": 18, "metric_value": 1.0, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Direction_same", "instances": 16, "metric_value": 0.9887, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[6]>2:
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
				if obj[6]>1:
					# {"feature": "Passanger", "instances": 414, "metric_value": 0.9926, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Education", "instances": 331, "metric_value": 0.977, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Direction_same", "instances": 302, "metric_value": 0.9674, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[2]>3:
							# {"feature": "Direction_same", "instances": 29, "metric_value": 0.9784, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[0]>2:
						# {"feature": "Education", "instances": 83, "metric_value": 0.9695, "depth": 6}
						if obj[2]>0:
							# {"feature": "Direction_same", "instances": 62, "metric_value": 0.988, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							# {"feature": "Direction_same", "instances": 21, "metric_value": 0.8631, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[6]<=1:
					# {"feature": "Direction_same", "instances": 235, "metric_value": 0.9757, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Passanger", "instances": 144, "metric_value": 0.9965, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Education", "instances": 132, "metric_value": 0.9993, "depth": 7}
							if obj[2]<=4:
								return 'True'
							elif obj[2]>4:
								return 'True'
							else: return 'True'
						elif obj[0]>2:
							# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 7}
							if obj[2]<=2:
								return 'True'
							elif obj[2]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[5]>0:
						# {"feature": "Education", "instances": 91, "metric_value": 0.9029, "depth": 6}
						if obj[2]>1:
							# {"feature": "Passanger", "instances": 54, "metric_value": 0.8524, "depth": 7}
							if obj[0]<=1:
								return 'True'
							else: return 'True'
						elif obj[2]<=1:
							# {"feature": "Passanger", "instances": 37, "metric_value": 0.9569, "depth": 7}
							if obj[0]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>13.710484759667237:
				# {"feature": "Direction_same", "instances": 115, "metric_value": 0.9154, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Education", "instances": 86, "metric_value": 0.9523, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Distance", "instances": 77, "metric_value": 0.9724, "depth": 6}
						if obj[6]>1:
							# {"feature": "Passanger", "instances": 57, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=2:
								return 'True'
							elif obj[0]>2:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							# {"feature": "Passanger", "instances": 20, "metric_value": 0.971, "depth": 7}
							if obj[0]<=1:
								return 'True'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[2]>3:
						# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[6]>1:
							# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[0]<=1:
								return 'True'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[5]>0:
					# {"feature": "Education", "instances": 29, "metric_value": 0.7355, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Distance", "instances": 23, "metric_value": 0.5586, "depth": 6}
						if obj[6]<=1:
							# {"feature": "Passanger", "instances": 17, "metric_value": 0.6723, "depth": 7}
							if obj[0]<=1:
								return 'True'
							else: return 'True'
						elif obj[6]>1:
							return 'True'
						else: return 'True'
					elif obj[2]>2:
						# {"feature": "Distance", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[6]>1:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=1:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
