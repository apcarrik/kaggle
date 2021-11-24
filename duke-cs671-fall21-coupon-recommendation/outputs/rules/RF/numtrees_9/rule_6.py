def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Occupation", "instances": 113, "metric_value": 0.9954, "depth": 1}
	if obj[12]<=11.504125348119867:
		# {"feature": "Coupon", "instances": 94, "metric_value": 0.9734, "depth": 2}
		if obj[5]>0:
			# {"feature": "Coffeehouse", "instances": 84, "metric_value": 0.9403, "depth": 3}
			if obj[15]>0.0:
				# {"feature": "Education", "instances": 59, "metric_value": 0.8432, "depth": 4}
				if obj[11]<=2:
					# {"feature": "Restaurant20to50", "instances": 48, "metric_value": 0.6962, "depth": 5}
					if obj[18]<=1.0:
						# {"feature": "Carryaway", "instances": 32, "metric_value": 0.8571, "depth": 6}
						if obj[16]>0.0:
							# {"feature": "Driving_to", "instances": 31, "metric_value": 0.8238, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Income", "instances": 23, "metric_value": 0.6666, "depth": 8}
								if obj[13]<=4:
									# {"feature": "Bar", "instances": 17, "metric_value": 0.7871, "depth": 9}
									if obj[14]>0.0:
										# {"feature": "Passanger", "instances": 11, "metric_value": 0.4395, "depth": 10}
										if obj[1]>1:
											return 'True'
										elif obj[1]<=1:
											# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[6]>0:
												# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7]>0:
													return 'False'
												elif obj[7]<=0:
													return 'True'
												else: return 'True'
											elif obj[6]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[14]<=0.0:
										# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 10}
										if obj[7]<=0:
											# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[4]>2:
												# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8]>0:
													return 'True'
												elif obj[8]<=0:
													return 'False'
												else: return 'False'
											elif obj[4]<=2:
												return 'False'
											else: return 'False'
										elif obj[7]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[13]>4:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								# {"feature": "Gender", "instances": 8, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Temperature", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[3]>30:
										return 'True'
									elif obj[3]<=30:
										# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[13]>2:
											return 'False'
										elif obj[13]<=2:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[7]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[16]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[18]>1.0:
						return 'True'
					else: return 'True'
				elif obj[11]>2:
					# {"feature": "Direction_same", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[19]<=0:
						# {"feature": "Restaurantlessthan20", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[17]>2.0:
							return 'False'
						elif obj[17]<=2.0:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4]<=2:
								return 'True'
							elif obj[4]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[19]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[15]<=0.0:
				# {"feature": "Time", "instances": 25, "metric_value": 0.9896, "depth": 4}
				if obj[4]<=3:
					# {"feature": "Restaurantlessthan20", "instances": 22, "metric_value": 1.0, "depth": 5}
					if obj[17]>1.0:
						# {"feature": "Driving_to", "instances": 17, "metric_value": 0.9774, "depth": 6}
						if obj[0]>0:
							# {"feature": "Weather", "instances": 12, "metric_value": 1.0, "depth": 7}
							if obj[2]<=1:
								# {"feature": "Temperature", "instances": 10, "metric_value": 0.971, "depth": 8}
								if obj[3]>30:
									# {"feature": "Age", "instances": 8, "metric_value": 1.0, "depth": 9}
									if obj[8]>2:
										# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[10]<=0:
											return 'True'
										elif obj[10]>0:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[19]>0:
												return 'True'
											elif obj[19]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[8]<=2:
										return 'False'
									else: return 'False'
								elif obj[3]<=30:
									return 'True'
								else: return 'True'
							elif obj[2]>1:
								return 'False'
							else: return 'False'
						elif obj[0]<=0:
							# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[8]>0:
								return 'True'
							elif obj[8]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[17]<=1.0:
						# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[8]<=4:
							return 'False'
						elif obj[8]>4:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[4]>3:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[5]<=0:
			# {"feature": "Distance", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[20]>1:
				return 'False'
			elif obj[20]<=1:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[12]>11.504125348119867:
		# {"feature": "Coupon", "instances": 19, "metric_value": 0.8315, "depth": 2}
		if obj[5]<=2:
			# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[11]>0:
				# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[4]>0:
					return 'False'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			elif obj[11]<=0:
				return 'True'
			else: return 'True'
		elif obj[5]>2:
			return 'False'
		else: return 'False'
	else: return 'False'
