def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Bar", "instances": 57, "metric_value": 0.9891, "depth": 2}
		if obj[12]<=2.0:
			# {"feature": "Coupon", "instances": 52, "metric_value": 0.9989, "depth": 3}
			if obj[3]<=3:
				# {"feature": "Income", "instances": 30, "metric_value": 0.9481, "depth": 4}
				if obj[11]<=6:
					# {"feature": "Age", "instances": 25, "metric_value": 0.9896, "depth": 5}
					if obj[6]<=6:
						# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 6}
						if obj[10]>4:
							# {"feature": "Maritalstatus", "instances": 15, "metric_value": 0.9968, "depth": 7}
							if obj[7]<=1:
								# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 8}
								if obj[9]<=2:
									# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[2]<=1:
										# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[1]<=0:
											# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[4]>0:
												return 'True'
											elif obj[4]<=0:
												# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[5]>0:
													return 'True'
												elif obj[5]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[1]>0:
											return 'False'
										else: return 'False'
									elif obj[2]>1:
										return 'True'
									else: return 'True'
								elif obj[9]>2:
									# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[2]<=1:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[5]>0:
											# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[13]>1.0:
												return 'False'
											elif obj[13]<=1.0:
												return 'True'
											else: return 'True'
										elif obj[5]<=0:
											return 'False'
										else: return 'False'
									elif obj[2]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[7]>1:
								return 'False'
							else: return 'False'
						elif obj[10]<=4:
							# {"feature": "Gender", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[6]>6:
						return 'False'
					else: return 'False'
				elif obj[11]>6:
					return 'True'
				else: return 'True'
			elif obj[3]>3:
				# {"feature": "Occupation", "instances": 22, "metric_value": 0.8454, "depth": 4}
				if obj[10]>4:
					# {"feature": "Time", "instances": 15, "metric_value": 0.971, "depth": 5}
					if obj[2]>0:
						# {"feature": "Gender", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[5]>0:
							return 'False'
						elif obj[5]<=0:
							# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[6]<=1:
								# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[8]<=0:
									return 'False'
								elif obj[8]>0:
									return 'True'
								else: return 'True'
							elif obj[6]>1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[10]<=4:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[12]>2.0:
			return 'False'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Coffeehouse", "instances": 28, "metric_value": 0.8113, "depth": 2}
		if obj[13]<=2.0:
			# {"feature": "Coupon", "instances": 22, "metric_value": 0.5746, "depth": 3}
			if obj[3]>2:
				return 'True'
			elif obj[3]<=2:
				# {"feature": "Time", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[9]<=2:
						# {"feature": "Income", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[11]>2:
							return 'True'
						elif obj[11]<=2:
							# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=1:
								return 'False'
							elif obj[1]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[9]>2:
						return 'False'
					else: return 'False'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[13]>2.0:
			# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[2]<=3:
				return 'False'
			elif obj[2]>3:
				# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[5]>0:
					return 'True'
				elif obj[5]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	else: return 'True'
