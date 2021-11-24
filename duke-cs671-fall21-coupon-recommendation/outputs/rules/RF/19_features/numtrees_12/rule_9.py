def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Education", "instances": 61, "metric_value": 0.967, "depth": 2}
		if obj[10]<=4:
			# {"feature": "Income", "instances": 58, "metric_value": 0.9444, "depth": 3}
			if obj[12]>3:
				# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 4}
				if obj[4]>0:
					# {"feature": "Distance", "instances": 26, "metric_value": 0.9612, "depth": 5}
					if obj[18]<=2:
						# {"feature": "Maritalstatus", "instances": 23, "metric_value": 0.8865, "depth": 6}
						if obj[8]>0:
							# {"feature": "Occupation", "instances": 16, "metric_value": 0.6962, "depth": 7}
							if obj[11]<=15:
								# {"feature": "Bar", "instances": 15, "metric_value": 0.5665, "depth": 8}
								if obj[13]>0.0:
									# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[14]>1.0:
										# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[7]<=4:
											# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[3]<=3:
												return 'True'
											elif obj[3]>3:
												# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[2]<=30:
													return 'True'
												elif obj[2]>30:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[7]>4:
											return 'False'
										else: return 'False'
									elif obj[14]<=1.0:
										return 'True'
									else: return 'True'
								elif obj[13]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[11]>15:
								return 'False'
							else: return 'False'
						elif obj[8]<=0:
							# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[3]<=1:
								# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[16]<=1.0:
									# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[14]<=2.0:
										return 'False'
									elif obj[14]>2.0:
										return 'True'
									else: return 'True'
								elif obj[16]>1.0:
									return 'True'
								else: return 'True'
							elif obj[3]>1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[18]>2:
						return 'False'
					else: return 'False'
				elif obj[4]<=0:
					# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[18]<=2:
						return 'False'
					elif obj[18]>2:
						# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6]<=0:
							return 'True'
						elif obj[6]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[12]<=3:
				# {"feature": "Coupon", "instances": 24, "metric_value": 0.65, "depth": 4}
				if obj[4]<=3:
					# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[14]<=2.0:
						# {"feature": "Age", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[7]<=2:
							return 'False'
						elif obj[7]>2:
							# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[2]>30:
								# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[5]<=0:
									return 'True'
								elif obj[5]>0:
									return 'False'
								else: return 'False'
							elif obj[2]<=30:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[14]>2.0:
						return 'True'
					else: return 'True'
				elif obj[4]>3:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[10]>4:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Distance", "instances": 24, "metric_value": 0.8113, "depth": 2}
		if obj[18]>1:
			# {"feature": "Temperature", "instances": 18, "metric_value": 0.9183, "depth": 3}
			if obj[2]<=55:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[11]<=19:
					return 'True'
				elif obj[11]>19:
					return 'False'
				else: return 'False'
			elif obj[2]>55:
				# {"feature": "Income", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[12]>1:
					# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[14]<=3.0:
						# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[6]>0:
							return 'False'
						elif obj[6]<=0:
							# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[7]>2:
								return 'False'
							elif obj[7]<=2:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[14]>3.0:
						return 'True'
					else: return 'True'
				elif obj[12]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[18]<=1:
			return 'True'
		else: return 'True'
	else: return 'True'
