def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.9849, "depth": 1}
	if obj[1]>1:
		# {"feature": "Distance", "instances": 5903, "metric_value": 0.9509, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Passanger", "instances": 5355, "metric_value": 0.936, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Restaurant20to50", "instances": 3134, "metric_value": 0.9633, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Occupation", "instances": 2530, "metric_value": 0.9542, "depth": 5}
					if obj[3]>0:
						# {"feature": "Direction_same", "instances": 2494, "metric_value": 0.9561, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Education", "instances": 1499, "metric_value": 0.9679, "depth": 7}
							if obj[2]>1:
								return 'True'
							elif obj[2]<=1:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							# {"feature": "Education", "instances": 995, "metric_value": 0.9347, "depth": 7}
							if obj[2]<=4:
								return 'True'
							elif obj[2]>4:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]<=0:
						# {"feature": "Direction_same", "instances": 36, "metric_value": 0.7107, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Education", "instances": 24, "metric_value": 0.8113, "depth": 7}
							if obj[2]<=0:
								return 'True'
							elif obj[2]>0:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							# {"feature": "Education", "instances": 12, "metric_value": 0.4138, "depth": 7}
							if obj[2]<=0:
								return 'True'
							elif obj[2]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					# {"feature": "Occupation", "instances": 604, "metric_value": 0.9903, "depth": 5}
					if obj[3]<=21:
						# {"feature": "Education", "instances": 591, "metric_value": 0.9923, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Direction_same", "instances": 515, "metric_value": 0.9963, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[2]>3:
							# {"feature": "Direction_same", "instances": 76, "metric_value": 0.9268, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]>21:
						# {"feature": "Direction_same", "instances": 13, "metric_value": 0.6194, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[2]<=0:
								return 'True'
							elif obj[2]>0:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>1:
				# {"feature": "Restaurant20to50", "instances": 2221, "metric_value": 0.8839, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Education", "instances": 1469, "metric_value": 0.9028, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Occupation", "instances": 1373, "metric_value": 0.9111, "depth": 6}
						if obj[3]>1.8220101660229062:
							# {"feature": "Direction_same", "instances": 1164, "metric_value": 0.9225, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[3]<=1.8220101660229062:
							# {"feature": "Direction_same", "instances": 209, "metric_value": 0.8315, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[2]>3:
						# {"feature": "Occupation", "instances": 96, "metric_value": 0.7383, "depth": 6}
						if obj[3]<=7:
							# {"feature": "Direction_same", "instances": 66, "metric_value": 0.8231, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[3]>7:
							# {"feature": "Direction_same", "instances": 30, "metric_value": 0.469, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>1.0:
					# {"feature": "Education", "instances": 752, "metric_value": 0.8414, "depth": 5}
					if obj[2]>1:
						# {"feature": "Occupation", "instances": 470, "metric_value": 0.876, "depth": 6}
						if obj[3]>4:
							# {"feature": "Direction_same", "instances": 343, "metric_value": 0.9113, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[3]<=4:
							# {"feature": "Direction_same", "instances": 127, "metric_value": 0.7464, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[2]<=1:
						# {"feature": "Occupation", "instances": 282, "metric_value": 0.7727, "depth": 6}
						if obj[3]<=21:
							# {"feature": "Direction_same", "instances": 278, "metric_value": 0.7784, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[3]>21:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[6]>2:
			# {"feature": "Passanger", "instances": 548, "metric_value": 0.9935, "depth": 3}
			if obj[0]>0:
				# {"feature": "Education", "instances": 534, "metric_value": 0.9903, "depth": 4}
				if obj[2]<=4:
					# {"feature": "Restaurant20to50", "instances": 531, "metric_value": 0.9892, "depth": 5}
					if obj[4]>-1.0:
						# {"feature": "Occupation", "instances": 528, "metric_value": 0.99, "depth": 6}
						if obj[3]<=7.621212121212121:
							# {"feature": "Direction_same", "instances": 337, "metric_value": 0.9954, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[3]>7.621212121212121:
							# {"feature": "Direction_same", "instances": 191, "metric_value": 0.9756, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[2]>4:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.5917, "depth": 4}
				if obj[4]<=1.0:
					return 'True'
				elif obj[4]>1.0:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[3]>1:
						# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[2]<=0:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[2]>0:
							return 'True'
						else: return 'True'
					elif obj[3]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Restaurant20to50", "instances": 2244, "metric_value": 0.982, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Passanger", "instances": 1483, "metric_value": 0.9482, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Education", "instances": 1258, "metric_value": 0.928, "depth": 4}
				if obj[2]>0:
					# {"feature": "Direction_same", "instances": 799, "metric_value": 0.8922, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Occupation", "instances": 617, "metric_value": 0.8646, "depth": 6}
						if obj[3]>0:
							# {"feature": "Distance", "instances": 616, "metric_value": 0.8631, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					elif obj[5]>0:
						# {"feature": "Occupation", "instances": 182, "metric_value": 0.9612, "depth": 6}
						if obj[3]<=17.9988432003742:
							# {"feature": "Distance", "instances": 168, "metric_value": 0.9737, "depth": 7}
							if obj[6]<=1:
								return 'False'
							elif obj[6]>1:
								return 'False'
							else: return 'False'
						elif obj[3]>17.9988432003742:
							# {"feature": "Distance", "instances": 14, "metric_value": 0.5917, "depth": 7}
							if obj[6]<=1:
								return 'False'
							elif obj[6]>1:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]<=0:
					# {"feature": "Occupation", "instances": 459, "metric_value": 0.9727, "depth": 5}
					if obj[3]>1.245339711559053:
						# {"feature": "Distance", "instances": 365, "metric_value": 0.9917, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Direction_same", "instances": 288, "metric_value": 0.9887, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[6]>2:
							# {"feature": "Direction_same", "instances": 77, "metric_value": 0.9989, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[3]<=1.245339711559053:
						# {"feature": "Distance", "instances": 94, "metric_value": 0.785, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 59, "metric_value": 0.694, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 35, "metric_value": 0.8981, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Occupation", "instances": 225, "metric_value": 1.0, "depth": 4}
				if obj[3]>0:
					# {"feature": "Education", "instances": 222, "metric_value": 0.9998, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Distance", "instances": 179, "metric_value": 0.9962, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 148, "metric_value": 0.9935, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 31, "metric_value": 0.9992, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[2]>2:
						# {"feature": "Distance", "instances": 43, "metric_value": 0.9682, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 37, "metric_value": 0.9569, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]>1.0:
			# {"feature": "Occupation", "instances": 761, "metric_value": 0.9979, "depth": 3}
			if obj[3]<=13.94152603856423:
				# {"feature": "Passanger", "instances": 642, "metric_value": 1.0, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Distance", "instances": 554, "metric_value": 0.9989, "depth": 5}
					if obj[6]>1:
						# {"feature": "Direction_same", "instances": 346, "metric_value": 0.9893, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Education", "instances": 309, "metric_value": 0.9945, "depth": 7}
							if obj[2]<=3:
								return 'False'
							elif obj[2]>3:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							# {"feature": "Education", "instances": 37, "metric_value": 0.878, "depth": 7}
							if obj[2]<=3:
								return 'False'
							elif obj[2]>3:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[6]<=1:
						# {"feature": "Direction_same", "instances": 208, "metric_value": 0.9933, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Education", "instances": 123, "metric_value": 0.9977, "depth": 7}
							if obj[2]<=4:
								return 'False'
							elif obj[2]>4:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							# {"feature": "Education", "instances": 85, "metric_value": 0.9259, "depth": 7}
							if obj[2]>1:
								return 'True'
							elif obj[2]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Education", "instances": 88, "metric_value": 0.9457, "depth": 5}
					if obj[2]>0:
						# {"feature": "Distance", "instances": 72, "metric_value": 0.9799, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 65, "metric_value": 0.9916, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[2]<=0:
						# {"feature": "Distance", "instances": 16, "metric_value": 0.5436, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 14, "metric_value": 0.5917, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>13.94152603856423:
				# {"feature": "Education", "instances": 119, "metric_value": 0.9211, "depth": 4}
				if obj[2]>0:
					# {"feature": "Distance", "instances": 64, "metric_value": 0.9887, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Passanger", "instances": 49, "metric_value": 0.9755, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 35, "metric_value": 0.9518, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							# {"feature": "Direction_same", "instances": 14, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]>2:
						# {"feature": "Passanger", "instances": 15, "metric_value": 0.9968, "depth": 6}
						if obj[0]>0:
							# {"feature": "Direction_same", "instances": 14, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]<=0:
					# {"feature": "Passanger", "instances": 55, "metric_value": 0.7568, "depth": 5}
					if obj[0]>0:
						# {"feature": "Distance", "instances": 45, "metric_value": 0.6236, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 31, "metric_value": 0.5548, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 14, "metric_value": 0.7496, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[0]<=0:
						# {"feature": "Direction_same", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 10, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1:
								return 'False'
							elif obj[6]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
