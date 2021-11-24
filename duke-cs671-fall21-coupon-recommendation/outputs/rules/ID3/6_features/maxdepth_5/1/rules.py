def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.9849, "depth": 1}
	if obj[1]>1:
		# {"feature": "Distance", "instances": 5903, "metric_value": 0.9509, "depth": 2}
		if obj[5]<=2:
			# {"feature": "Passanger", "instances": 5355, "metric_value": 0.936, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Restaurant20to50", "instances": 3134, "metric_value": 0.9633, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Occupation", "instances": 2530, "metric_value": 0.9542, "depth": 5}
					if obj[3]>0:
						# {"feature": "Education", "instances": 2494, "metric_value": 0.9561, "depth": 6}
						if obj[2]<=4:
							return 'True'
						elif obj[2]>4:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						# {"feature": "Education", "instances": 36, "metric_value": 0.7107, "depth": 6}
						if obj[2]<=0:
							return 'True'
						elif obj[2]>0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					# {"feature": "Occupation", "instances": 604, "metric_value": 0.9903, "depth": 5}
					if obj[3]<=21:
						# {"feature": "Education", "instances": 591, "metric_value": 0.9923, "depth": 6}
						if obj[2]<=3:
							return 'True'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					elif obj[3]>21:
						# {"feature": "Education", "instances": 13, "metric_value": 0.6194, "depth": 6}
						if obj[2]<=0:
							return 'True'
						elif obj[2]>0:
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
							return 'True'
						elif obj[3]<=1.8220101660229062:
							return 'True'
						else: return 'True'
					elif obj[2]>3:
						# {"feature": "Occupation", "instances": 96, "metric_value": 0.7383, "depth": 6}
						if obj[3]<=7:
							return 'True'
						elif obj[3]>7:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>1.0:
					# {"feature": "Education", "instances": 752, "metric_value": 0.8414, "depth": 5}
					if obj[2]>1:
						# {"feature": "Occupation", "instances": 470, "metric_value": 0.876, "depth": 6}
						if obj[3]>4:
							return 'True'
						elif obj[3]<=4:
							return 'True'
						else: return 'True'
					elif obj[2]<=1:
						# {"feature": "Occupation", "instances": 282, "metric_value": 0.7727, "depth": 6}
						if obj[3]<=21:
							return 'True'
						elif obj[3]>21:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[5]>2:
			# {"feature": "Passanger", "instances": 548, "metric_value": 0.9935, "depth": 3}
			if obj[0]>0:
				# {"feature": "Education", "instances": 534, "metric_value": 0.9903, "depth": 4}
				if obj[2]<=4:
					# {"feature": "Restaurant20to50", "instances": 531, "metric_value": 0.9892, "depth": 5}
					if obj[4]>-1.0:
						# {"feature": "Occupation", "instances": 528, "metric_value": 0.99, "depth": 6}
						if obj[3]<=7.621212121212121:
							return 'False'
						elif obj[3]>7.621212121212121:
							return 'False'
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
							return 'True'
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
					# {"feature": "Occupation", "instances": 799, "metric_value": 0.8922, "depth": 5}
					if obj[3]<=13.433985321674566:
						# {"feature": "Distance", "instances": 679, "metric_value": 0.9087, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[3]>13.433985321674566:
						# {"feature": "Distance", "instances": 120, "metric_value": 0.7692, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]<=0:
					# {"feature": "Occupation", "instances": 459, "metric_value": 0.9727, "depth": 5}
					if obj[3]>1.245339711559053:
						# {"feature": "Distance", "instances": 365, "metric_value": 0.9917, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'False'
						else: return 'False'
					elif obj[3]<=1.245339711559053:
						# {"feature": "Distance", "instances": 94, "metric_value": 0.785, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Occupation", "instances": 225, "metric_value": 1.0, "depth": 4}
				if obj[3]>0:
					# {"feature": "Education", "instances": 222, "metric_value": 0.9998, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Distance", "instances": 179, "metric_value": 0.9962, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[2]>2:
						# {"feature": "Distance", "instances": 43, "metric_value": 0.9682, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
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
					if obj[5]>1:
						# {"feature": "Education", "instances": 346, "metric_value": 0.9893, "depth": 6}
						if obj[2]<=3:
							return 'False'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					elif obj[5]<=1:
						# {"feature": "Education", "instances": 208, "metric_value": 0.9933, "depth": 6}
						if obj[2]<=4:
							return 'True'
						elif obj[2]>4:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Education", "instances": 88, "metric_value": 0.9457, "depth": 5}
					if obj[2]>0:
						# {"feature": "Distance", "instances": 72, "metric_value": 0.9799, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						# {"feature": "Distance", "instances": 16, "metric_value": 0.5436, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>13.94152603856423:
				# {"feature": "Education", "instances": 119, "metric_value": 0.9211, "depth": 4}
				if obj[2]>0:
					# {"feature": "Distance", "instances": 64, "metric_value": 0.9887, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Passanger", "instances": 49, "metric_value": 0.9755, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					elif obj[5]>2:
						# {"feature": "Passanger", "instances": 15, "metric_value": 0.9968, "depth": 6}
						if obj[0]>0:
							return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]<=0:
					# {"feature": "Passanger", "instances": 55, "metric_value": 0.7568, "depth": 5}
					if obj[0]>0:
						# {"feature": "Distance", "instances": 45, "metric_value": 0.6236, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						# {"feature": "Distance", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[5]<=1:
							return 'False'
						elif obj[5]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
