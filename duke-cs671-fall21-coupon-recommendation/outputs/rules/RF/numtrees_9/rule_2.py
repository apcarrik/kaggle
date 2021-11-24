def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Passanger", "instances": 113, "metric_value": 0.9972, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Income", "instances": 78, "metric_value": 0.9881, "depth": 2}
		if obj[13]<=6:
			# {"feature": "Occupation", "instances": 67, "metric_value": 0.953, "depth": 3}
			if obj[12]<=19.500092512278858:
				# {"feature": "Time", "instances": 64, "metric_value": 0.9284, "depth": 4}
				if obj[4]>0:
					# {"feature": "Driving_to", "instances": 47, "metric_value": 0.8196, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Restaurantlessthan20", "instances": 41, "metric_value": 0.8722, "depth": 6}
						if obj[17]<=3.0:
							# {"feature": "Coffeehouse", "instances": 35, "metric_value": 0.9275, "depth": 7}
							if obj[15]<=3.0:
								# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.9629, "depth": 8}
								if obj[18]>0.0:
									# {"feature": "Coupon_validity", "instances": 27, "metric_value": 0.9911, "depth": 9}
									if obj[6]>0:
										# {"feature": "Age", "instances": 16, "metric_value": 0.8113, "depth": 10}
										if obj[8]>2:
											# {"feature": "Maritalstatus", "instances": 10, "metric_value": 0.971, "depth": 11}
											if obj[9]<=1:
												# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 12}
												if obj[5]>2:
													return 'False'
												elif obj[5]<=2:
													# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[9]>1:
												return 'True'
											else: return 'True'
										elif obj[8]<=2:
											return 'False'
										else: return 'False'
									elif obj[6]<=0:
										# {"feature": "Coupon", "instances": 11, "metric_value": 0.8454, "depth": 10}
										if obj[5]>0:
											return 'True'
										elif obj[5]<=0:
											# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[14]<=0.0:
												return 'False'
											elif obj[14]>0.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								elif obj[18]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[15]>3.0:
								return 'False'
							else: return 'False'
						elif obj[17]>3.0:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				elif obj[4]<=0:
					# {"feature": "Coupon", "instances": 17, "metric_value": 0.9774, "depth": 5}
					if obj[5]>0:
						# {"feature": "Bar", "instances": 14, "metric_value": 0.8631, "depth": 6}
						if obj[14]>0.0:
							# {"feature": "Temperature", "instances": 9, "metric_value": 0.5033, "depth": 7}
							if obj[3]<=55:
								return 'True'
							elif obj[3]>55:
								# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[14]<=0.0:
							# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[7]<=0:
								# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3]>55:
									return 'True'
								elif obj[3]<=55:
									return 'False'
								else: return 'False'
							elif obj[7]>0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[5]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[12]>19.500092512278858:
				return 'True'
			else: return 'True'
		elif obj[13]>6:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[5]<=3:
				return 'True'
			elif obj[5]>3:
				# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=55:
						return 'False'
					elif obj[3]>55:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[1]>2:
		# {"feature": "Bar", "instances": 35, "metric_value": 0.8224, "depth": 2}
		if obj[14]>0.0:
			# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.9819, "depth": 3}
			if obj[15]>0.0:
				# {"feature": "Time", "instances": 14, "metric_value": 0.8631, "depth": 4}
				if obj[4]>0:
					# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[12]<=12:
						return 'True'
					elif obj[12]>12:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=1:
							return 'True'
						elif obj[5]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]<=0:
					# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[8]<=3:
						return 'False'
					elif obj[8]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[15]<=0.0:
				# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[9]>0:
					return 'False'
				elif obj[9]<=0:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>2:
						return 'True'
					elif obj[4]<=2:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[14]<=0.0:
			# {"feature": "Carryaway", "instances": 16, "metric_value": 0.3373, "depth": 3}
			if obj[16]<=3.0:
				return 'True'
			elif obj[16]>3.0:
				# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[20]<=1:
					return 'False'
				elif obj[20]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	else: return 'True'
