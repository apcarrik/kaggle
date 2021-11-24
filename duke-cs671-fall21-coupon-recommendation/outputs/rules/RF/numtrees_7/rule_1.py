def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 146, "metric_value": 0.9988, "depth": 1}
	if obj[5]>0:
		# {"feature": "Coupon_validity", "instances": 122, "metric_value": 0.9842, "depth": 2}
		if obj[6]>0:
			# {"feature": "Occupation", "instances": 63, "metric_value": 0.9911, "depth": 3}
			if obj[12]<=12:
				# {"feature": "Education", "instances": 56, "metric_value": 1.0, "depth": 4}
				if obj[11]>1:
					# {"feature": "Temperature", "instances": 31, "metric_value": 0.9072, "depth": 5}
					if obj[3]>55:
						# {"feature": "Coffeehouse", "instances": 18, "metric_value": 1.0, "depth": 6}
						if obj[15]>0.0:
							# {"feature": "Driving_to", "instances": 15, "metric_value": 0.971, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Bar", "instances": 13, "metric_value": 0.8905, "depth": 8}
								if obj[14]>0.0:
									# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.971, "depth": 9}
									if obj[18]>0.0:
										# {"feature": "Age", "instances": 8, "metric_value": 1.0, "depth": 10}
										if obj[8]>2:
											# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[1]>2:
												# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[13]>0:
													return 'True'
												elif obj[13]<=0:
													return 'False'
												else: return 'False'
											elif obj[1]<=2:
												return 'False'
											else: return 'False'
										elif obj[8]<=2:
											# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[4]>0:
												return 'True'
											elif obj[4]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[18]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[14]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						elif obj[15]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[3]<=55:
						# {"feature": "Age", "instances": 13, "metric_value": 0.3912, "depth": 6}
						if obj[8]>0:
							return 'False'
						elif obj[8]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[11]<=1:
					# {"feature": "Carryaway", "instances": 25, "metric_value": 0.8555, "depth": 5}
					if obj[16]>1.0:
						# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.6098, "depth": 6}
						if obj[15]<=1.0:
							return 'True'
						elif obj[15]>1.0:
							# {"feature": "Bar", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[14]>0.0:
								# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[17]>1.0:
									# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]<=0:
										return 'True'
									elif obj[0]>0:
										return 'False'
									else: return 'False'
								elif obj[17]<=1.0:
									return 'False'
								else: return 'False'
							elif obj[14]<=0.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[16]<=1.0:
						# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[4]<=1:
							return 'False'
						elif obj[4]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[12]>12:
				return 'False'
			else: return 'False'
		elif obj[6]<=0:
			# {"feature": "Income", "instances": 59, "metric_value": 0.8663, "depth": 3}
			if obj[13]<=6:
				# {"feature": "Restaurant20to50", "instances": 48, "metric_value": 0.9377, "depth": 4}
				if obj[18]>0.0:
					# {"feature": "Distance", "instances": 37, "metric_value": 0.8419, "depth": 5}
					if obj[20]<=1:
						# {"feature": "Passanger", "instances": 20, "metric_value": 0.6098, "depth": 6}
						if obj[1]<=1:
							return 'True'
						elif obj[1]>1:
							# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[12]>4:
								# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[4]<=2:
									return 'False'
								elif obj[4]>2:
									return 'True'
								else: return 'True'
							elif obj[12]<=4:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[20]>1:
						# {"feature": "Age", "instances": 17, "metric_value": 0.9774, "depth": 6}
						if obj[8]>0:
							# {"feature": "Passanger", "instances": 15, "metric_value": 0.9183, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[11]>1:
									# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[14]<=1.0:
										return 'True'
									elif obj[14]>1.0:
										return 'False'
									else: return 'False'
								elif obj[11]<=1:
									return 'False'
								else: return 'False'
							elif obj[1]>1:
								return 'True'
							else: return 'True'
						elif obj[8]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[18]<=0.0:
					# {"feature": "Passanger", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[1]<=1:
						return 'False'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[13]>6:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[5]<=0:
		# {"feature": "Children", "instances": 24, "metric_value": 0.8113, "depth": 2}
		if obj[10]<=0:
			# {"feature": "Maritalstatus", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[9]<=1:
				# {"feature": "Income", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[13]>3:
					return 'False'
				elif obj[13]<=3:
					# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2]<=0:
						return 'True'
					elif obj[2]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[9]>1:
				return 'True'
			else: return 'True'
		elif obj[10]>0:
			return 'False'
		else: return 'False'
	else: return 'False'
