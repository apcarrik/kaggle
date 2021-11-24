def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Bar", "instances": 127, "metric_value": 0.9964, "depth": 1}
	if obj[13]<=1.0:
		# {"feature": "Age", "instances": 86, "metric_value": 0.9965, "depth": 2}
		if obj[7]<=4:
			# {"feature": "Gender", "instances": 66, "metric_value": 0.976, "depth": 3}
			if obj[6]<=0:
				# {"feature": "Restaurantlessthan20", "instances": 33, "metric_value": 0.8454, "depth": 4}
				if obj[15]<=2.0:
					# {"feature": "Education", "instances": 25, "metric_value": 0.9427, "depth": 5}
					if obj[10]<=2:
						# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.9928, "depth": 6}
						if obj[16]>0.0:
							# {"feature": "Maritalstatus", "instances": 17, "metric_value": 0.9367, "depth": 7}
							if obj[8]>0:
								# {"feature": "Income", "instances": 10, "metric_value": 1.0, "depth": 8}
								if obj[12]>2:
									# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[14]>-1.0:
										# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 10}
										if obj[18]<=2:
											# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[0]>1:
												# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[1]<=0:
													# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[4]<=2:
														return 'True'
													elif obj[4]>2:
														return 'False'
													else: return 'False'
												elif obj[1]>0:
													return 'False'
												else: return 'False'
											elif obj[0]<=1:
												return 'False'
											else: return 'False'
										elif obj[18]>2:
											return 'True'
										else: return 'True'
									elif obj[14]<=-1.0:
										return 'True'
									else: return 'True'
								elif obj[12]<=2:
									return 'True'
								else: return 'True'
							elif obj[8]<=0:
								# {"feature": "Temperature", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[2]>55:
									return 'False'
								elif obj[2]<=55:
									# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[4]<=3:
										return 'False'
									elif obj[4]>3:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						elif obj[16]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[10]>2:
						return 'False'
					else: return 'False'
				elif obj[15]>2.0:
					return 'False'
				else: return 'False'
			elif obj[6]>0:
				# {"feature": "Time", "instances": 33, "metric_value": 0.994, "depth": 4}
				if obj[3]<=1:
					# {"feature": "Income", "instances": 22, "metric_value": 0.9457, "depth": 5}
					if obj[12]<=5:
						# {"feature": "Occupation", "instances": 17, "metric_value": 0.9975, "depth": 6}
						if obj[11]>4:
							# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[18]<=2:
								# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 8}
								if obj[16]>0.0:
									return 'True'
								elif obj[16]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[18]>2:
								return 'False'
							else: return 'False'
						elif obj[11]<=4:
							# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[10]>0:
								return 'False'
							elif obj[10]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[12]>5:
						return 'False'
					else: return 'False'
				elif obj[3]>1:
					# {"feature": "Occupation", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[11]<=14:
						return 'True'
					elif obj[11]>14:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[7]>4:
			# {"feature": "Restaurantlessthan20", "instances": 20, "metric_value": 0.9341, "depth": 3}
			if obj[15]<=2.0:
				# {"feature": "Occupation", "instances": 14, "metric_value": 0.7496, "depth": 4}
				if obj[11]<=5:
					# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[14]>0.0:
						# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[18]>1:
							return 'False'
						elif obj[18]<=1:
							return 'True'
						else: return 'True'
					elif obj[14]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[11]>5:
					return 'True'
				else: return 'True'
			elif obj[15]>2.0:
				# {"feature": "Coupon_validity", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=55:
						return 'True'
					elif obj[2]>55:
						return 'False'
					else: return 'False'
				elif obj[5]>0:
					return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[13]>1.0:
		# {"feature": "Time", "instances": 41, "metric_value": 0.9012, "depth": 2}
		if obj[3]<=1:
			# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 3}
			if obj[11]<=7:
				# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[10]>0:
					return 'True'
				elif obj[10]<=0:
					# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[7]>1:
							return 'False'
						elif obj[7]<=1:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[11]>7:
				# {"feature": "Temperature", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[2]<=55:
					# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[4]>0:
						return 'False'
					elif obj[4]<=0:
						# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[2]>55:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[7]<=3:
						return 'True'
					elif obj[7]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[3]>1:
			# {"feature": "Occupation", "instances": 18, "metric_value": 0.5033, "depth": 3}
			if obj[11]>1:
				return 'True'
			elif obj[11]<=1:
				# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[4]<=2:
					return 'True'
				elif obj[4]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	else: return 'True'
