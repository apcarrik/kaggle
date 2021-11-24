def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coffeehouse", "instances": 127, "metric_value": 0.9989, "depth": 1}
	if obj[15]>1.0:
		# {"feature": "Bar", "instances": 65, "metric_value": 0.9501, "depth": 2}
		if obj[14]<=1.0:
			# {"feature": "Coupon", "instances": 41, "metric_value": 0.839, "depth": 3}
			if obj[5]>0:
				# {"feature": "Education", "instances": 35, "metric_value": 0.661, "depth": 4}
				if obj[11]>1:
					# {"feature": "Temperature", "instances": 24, "metric_value": 0.8113, "depth": 5}
					if obj[3]>55:
						# {"feature": "Occupation", "instances": 15, "metric_value": 0.3534, "depth": 6}
						if obj[12]>2:
							return 'True'
						elif obj[12]<=2:
							# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>0:
								return 'True'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[3]<=55:
						# {"feature": "Children", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[10]<=0:
							# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[13]<=4:
								return 'True'
							elif obj[13]>4:
								return 'False'
							else: return 'False'
						elif obj[10]>0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[11]<=1:
					return 'True'
				else: return 'True'
			elif obj[5]<=0:
				# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[8]>1:
					return 'False'
				elif obj[8]<=1:
					# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[14]>1.0:
			# {"feature": "Driving_to", "instances": 24, "metric_value": 0.995, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Distance", "instances": 20, "metric_value": 0.9928, "depth": 4}
				if obj[19]<=2:
					# {"feature": "Time", "instances": 18, "metric_value": 1.0, "depth": 5}
					if obj[4]<=1:
						# {"feature": "Children", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[10]<=0:
							return 'False'
						elif obj[10]>0:
							return 'True'
						else: return 'True'
					elif obj[4]>1:
						# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[11]<=2:
							return 'True'
						elif obj[11]>2:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=3:
								return 'False'
							elif obj[5]>3:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[19]>2:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[15]<=1.0:
		# {"feature": "Bar", "instances": 62, "metric_value": 0.9728, "depth": 2}
		if obj[14]<=1.0:
			# {"feature": "Coupon", "instances": 50, "metric_value": 0.9044, "depth": 3}
			if obj[5]>0:
				# {"feature": "Restaurantlessthan20", "instances": 40, "metric_value": 0.971, "depth": 4}
				if obj[16]>1.0:
					# {"feature": "Income", "instances": 29, "metric_value": 0.9991, "depth": 5}
					if obj[13]<=3:
						# {"feature": "Occupation", "instances": 16, "metric_value": 0.896, "depth": 6}
						if obj[12]>2:
							# {"feature": "Age", "instances": 14, "metric_value": 0.7496, "depth": 7}
							if obj[8]<=4:
								# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 8}
								if obj[17]<=1.0:
									# {"feature": "Distance", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[19]>1:
										return 'False'
									elif obj[19]<=1:
										# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[0]<=0:
											# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[11]>0:
												return 'False'
											elif obj[11]<=0:
												return 'True'
											else: return 'True'
										elif obj[0]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[17]>1.0:
									return 'True'
								else: return 'True'
							elif obj[8]>4:
								return 'False'
							else: return 'False'
						elif obj[12]<=2:
							return 'True'
						else: return 'True'
					elif obj[13]>3:
						# {"feature": "Occupation", "instances": 13, "metric_value": 0.7793, "depth": 6}
						if obj[12]>1:
							# {"feature": "Direction_same", "instances": 12, "metric_value": 0.65, "depth": 7}
							if obj[18]<=0:
								# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 8}
								if obj[11]<=2:
									return 'True'
								elif obj[11]>2:
									# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1]>0:
										return 'True'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[18]>0:
								return 'False'
							else: return 'False'
						elif obj[12]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[16]<=1.0:
					# {"feature": "Age", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[8]<=3:
						return 'False'
					elif obj[8]>3:
						# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=0:
							return 'False'
						elif obj[0]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[5]<=0:
				return 'False'
			else: return 'False'
		elif obj[14]>1.0:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[5]>2:
				# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[9]>0:
						return 'True'
					elif obj[9]<=0:
						return 'False'
					else: return 'False'
				elif obj[4]>2:
					return 'False'
				else: return 'False'
			elif obj[5]<=2:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
