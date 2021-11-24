def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 146, "metric_value": 0.9966, "depth": 1}
	if obj[5]>0:
		# {"feature": "Income", "instances": 116, "metric_value": 0.9576, "depth": 2}
		if obj[13]>3:
			# {"feature": "Carryaway", "instances": 60, "metric_value": 0.8366, "depth": 3}
			if obj[16]>1.0:
				# {"feature": "Bar", "instances": 44, "metric_value": 0.6321, "depth": 4}
				if obj[14]>0.0:
					# {"feature": "Weather", "instances": 23, "metric_value": 0.8281, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Coupon_validity", "instances": 18, "metric_value": 0.9183, "depth": 6}
						if obj[6]>0:
							# {"feature": "Restaurantlessthan20", "instances": 10, "metric_value": 1.0, "depth": 7}
							if obj[17]<=2.0:
								# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[8]>2:
									return 'True'
								elif obj[8]<=2:
									# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[11]<=2:
										return 'False'
									elif obj[11]>2:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[17]>2.0:
								return 'False'
							else: return 'False'
						elif obj[6]<=0:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[19]<=0:
								return 'True'
							elif obj[19]>0:
								# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[8]<=1:
									return 'True'
								elif obj[8]>1:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[2]>0:
						return 'True'
					else: return 'True'
				elif obj[14]<=0.0:
					# {"feature": "Age", "instances": 21, "metric_value": 0.2762, "depth": 5}
					if obj[8]<=6:
						return 'True'
					elif obj[8]>6:
						# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]>30:
							return 'False'
						elif obj[3]<=30:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[16]<=1.0:
				# {"feature": "Weather", "instances": 16, "metric_value": 0.9887, "depth": 4}
				if obj[2]<=0:
					# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[11]>0:
						return 'True'
					elif obj[11]<=0:
						# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[9]>0:
							return 'False'
						elif obj[9]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]>0:
					# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[9]<=1:
						return 'False'
					elif obj[9]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[13]<=3:
			# {"feature": "Coffeehouse", "instances": 56, "metric_value": 1.0, "depth": 3}
			if obj[15]>0.0:
				# {"feature": "Restaurant20to50", "instances": 44, "metric_value": 0.976, "depth": 4}
				if obj[18]>0.0:
					# {"feature": "Occupation", "instances": 42, "metric_value": 0.9587, "depth": 5}
					if obj[12]>2:
						# {"feature": "Age", "instances": 35, "metric_value": 0.8981, "depth": 6}
						if obj[8]<=1:
							# {"feature": "Carryaway", "instances": 18, "metric_value": 0.5033, "depth": 7}
							if obj[16]>1.0:
								# {"feature": "Time", "instances": 17, "metric_value": 0.3228, "depth": 8}
								if obj[4]>0:
									return 'True'
								elif obj[4]<=0:
									# {"feature": "Driving_to", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[0]>0:
										return 'True'
									elif obj[0]<=0:
										# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1]<=0:
											return 'True'
										elif obj[1]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[16]<=1.0:
								return 'False'
							else: return 'False'
						elif obj[8]>1:
							# {"feature": "Maritalstatus", "instances": 17, "metric_value": 0.9975, "depth": 7}
							if obj[9]>0:
								# {"feature": "Passanger", "instances": 13, "metric_value": 0.9612, "depth": 8}
								if obj[1]>0:
									# {"feature": "Distance", "instances": 11, "metric_value": 0.8454, "depth": 9}
									if obj[20]>1:
										# {"feature": "Weather", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[2]<=0:
											# {"feature": "Driving_to", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[6]<=0:
													return 'True'
												elif obj[6]>0:
													return 'False'
												else: return 'False'
											elif obj[0]>1:
												return 'False'
											else: return 'False'
										elif obj[2]>0:
											return 'True'
										else: return 'True'
									elif obj[20]<=1:
										return 'True'
									else: return 'True'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							elif obj[9]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[12]<=2:
						# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[8]<=4:
							return 'False'
						elif obj[8]>4:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[18]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[15]<=0.0:
				# {"feature": "Age", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[8]>0:
					return 'False'
				elif obj[8]<=0:
					# {"feature": "Coupon_validity", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[6]>0:
						return 'True'
					elif obj[6]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[5]<=0:
		# {"feature": "Coffeehouse", "instances": 30, "metric_value": 0.7219, "depth": 2}
		if obj[15]>1.0:
			# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.9367, "depth": 3}
			if obj[18]<=1.0:
				# {"feature": "Carryaway", "instances": 12, "metric_value": 1.0, "depth": 4}
				if obj[16]<=2.0:
					# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[8]<=6:
						return 'True'
					elif obj[8]>6:
						return 'False'
					else: return 'False'
				elif obj[16]>2.0:
					# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[11]>0:
						return 'False'
					elif obj[11]<=0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[18]>1.0:
				return 'False'
			else: return 'False'
		elif obj[15]<=1.0:
			return 'False'
		else: return 'False'
	else: return 'False'
