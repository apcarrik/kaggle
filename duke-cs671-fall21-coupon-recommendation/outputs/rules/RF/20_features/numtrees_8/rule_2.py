def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Temperature", "instances": 127, "metric_value": 0.9762, "depth": 1}
	if obj[3]>55:
		# {"feature": "Restaurantlessthan20", "instances": 66, "metric_value": 0.799, "depth": 2}
		if obj[16]<=3.0:
			# {"feature": "Age", "instances": 58, "metric_value": 0.7007, "depth": 3}
			if obj[8]>1:
				# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.8582, "depth": 4}
				if obj[17]<=1.0:
					# {"feature": "Income", "instances": 30, "metric_value": 0.9481, "depth": 5}
					if obj[13]>3:
						# {"feature": "Occupation", "instances": 19, "metric_value": 0.7425, "depth": 6}
						if obj[12]<=10:
							# {"feature": "Bar", "instances": 12, "metric_value": 0.9183, "depth": 7}
							if obj[14]<=1.0:
								# {"feature": "Gender", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[7]>0:
									# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[9]>0:
										return 'True'
									elif obj[9]<=0:
										# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[15]<=0.0:
											return 'True'
										elif obj[15]>0.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[7]<=0:
									return 'False'
								else: return 'False'
							elif obj[14]>1.0:
								return 'True'
							else: return 'True'
						elif obj[12]>10:
							return 'True'
						else: return 'True'
					elif obj[13]<=3:
						# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[15]<=1.0:
							return 'False'
						elif obj[15]>1.0:
							# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[4]<=1:
								return 'True'
							elif obj[4]>1:
								# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5]>2:
									return 'True'
								elif obj[5]<=2:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[17]>1.0:
					return 'True'
				else: return 'True'
			elif obj[8]<=1:
				return 'True'
			else: return 'True'
		elif obj[16]>3.0:
			# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[4]>0:
				# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[10]<=0:
					return 'True'
				elif obj[10]>0:
					return 'False'
				else: return 'False'
			elif obj[4]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[3]<=55:
		# {"feature": "Passanger", "instances": 61, "metric_value": 0.9764, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Time", "instances": 49, "metric_value": 0.9113, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Driving_to", "instances": 44, "metric_value": 0.9457, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Occupation", "instances": 34, "metric_value": 0.874, "depth": 5}
					if obj[12]<=12:
						# {"feature": "Coffeehouse", "instances": 29, "metric_value": 0.9294, "depth": 6}
						if obj[15]<=2.0:
							# {"feature": "Income", "instances": 25, "metric_value": 0.8555, "depth": 7}
							if obj[13]<=6:
								# {"feature": "Bar", "instances": 18, "metric_value": 0.9641, "depth": 8}
								if obj[14]>0.0:
									# {"feature": "Direction_same", "instances": 10, "metric_value": 0.7219, "depth": 9}
									if obj[18]<=0:
										return 'False'
									elif obj[18]>0:
										# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[6]<=0:
											return 'True'
										elif obj[6]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[14]<=0.0:
									# {"feature": "Weather", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[2]<=1:
										# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[5]>0:
											return 'True'
										elif obj[5]<=0:
											return 'False'
										else: return 'False'
									elif obj[2]>1:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[13]>6:
								return 'False'
							else: return 'False'
						elif obj[15]>2.0:
							# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[12]>12:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					# {"feature": "Children", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[10]<=0:
						# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[15]>1.0:
							# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[11]>0:
								# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[12]<=9:
									return 'False'
								elif obj[12]>9:
									return 'True'
								else: return 'True'
							elif obj[11]<=0:
								return 'True'
							else: return 'True'
						elif obj[15]<=1.0:
							return 'False'
						else: return 'False'
					elif obj[10]>0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]>2:
				return 'False'
			else: return 'False'
		elif obj[1]>2:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[5]>1:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[17]<=2.0:
					return 'True'
				elif obj[17]>2.0:
					return 'False'
				else: return 'False'
			elif obj[5]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
