def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Distance", "instances": 127, "metric_value": 0.9445, "depth": 1}
	if obj[7]<=2:
		# {"feature": "Education", "instances": 109, "metric_value": 0.8954, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Occupation", "instances": 105, "metric_value": 0.9085, "depth": 3}
			if obj[3]<=7:
				# {"feature": "Passanger", "instances": 72, "metric_value": 0.9544, "depth": 4}
				if obj[0]>0:
					# {"feature": "Restaurant20to50", "instances": 66, "metric_value": 0.976, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Bar", "instances": 46, "metric_value": 0.9986, "depth": 6}
						if obj[4]>-1.0:
							# {"feature": "Coupon", "instances": 45, "metric_value": 0.9968, "depth": 7}
							if obj[1]>0:
								# {"feature": "Direction_same", "instances": 41, "metric_value": 0.9892, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[4]<=-1.0:
							return 'False'
						else: return 'False'
					elif obj[5]>1.0:
						# {"feature": "Coupon", "instances": 20, "metric_value": 0.8113, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Bar", "instances": 11, "metric_value": 0.4395, "depth": 7}
							if obj[4]>1.0:
								return 'True'
							elif obj[4]<=1.0:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]>3:
							# {"feature": "Bar", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[4]<=1.0:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[4]>1.0:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[3]>7:
				# {"feature": "Direction_same", "instances": 33, "metric_value": 0.7455, "depth": 4}
				if obj[6]<=0:
					# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.8404, "depth": 5}
					if obj[5]<=2.0:
						# {"feature": "Bar", "instances": 25, "metric_value": 0.795, "depth": 6}
						if obj[4]<=1.0:
							# {"feature": "Coupon", "instances": 19, "metric_value": 0.8997, "depth": 7}
							if obj[1]>0:
								# {"feature": "Passanger", "instances": 15, "metric_value": 0.7219, "depth": 8}
								if obj[0]>0:
									return 'True'
								elif obj[0]<=0:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[0]<=1:
									return 'False'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					elif obj[5]>2.0:
						return 'False'
					else: return 'False'
				elif obj[6]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]>3:
			return 'True'
		else: return 'True'
	elif obj[7]>2:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[3]<=12:
				# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[2]>0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[2]<=0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[5]>1.0:
						return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[3]>12:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[3]<=11:
				return 'False'
			elif obj[3]>11:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
