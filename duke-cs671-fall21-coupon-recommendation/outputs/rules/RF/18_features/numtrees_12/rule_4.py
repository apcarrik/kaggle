def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9879, "depth": 1}
	if obj[3]>1:
		# {"feature": "Coffeehouse", "instances": 62, "metric_value": 0.9072, "depth": 2}
		if obj[13]<=1.0:
			# {"feature": "Income", "instances": 35, "metric_value": 0.9947, "depth": 3}
			if obj[11]<=6:
				# {"feature": "Occupation", "instances": 31, "metric_value": 0.9992, "depth": 4}
				if obj[10]>3:
					# {"feature": "Bar", "instances": 26, "metric_value": 0.9829, "depth": 5}
					if obj[12]<=2.0:
						# {"feature": "Education", "instances": 23, "metric_value": 0.9321, "depth": 6}
						if obj[9]<=2:
							# {"feature": "Coupon_validity", "instances": 14, "metric_value": 0.5917, "depth": 7}
							if obj[4]>0:
								# {"feature": "Weather", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[1]<=0:
									# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 9}
									if obj[2]<=2:
										return 'True'
									elif obj[2]>2:
										# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5]<=0:
											return 'True'
										elif obj[5]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[1]>0:
									return 'False'
								else: return 'False'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						elif obj[9]>2:
							# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[17]>1:
								# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[0]>1:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[5]<=0:
										return 'False'
									elif obj[5]>0:
										return 'True'
									else: return 'True'
								elif obj[0]<=1:
									return 'True'
								else: return 'True'
							elif obj[17]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[12]>2.0:
						return 'False'
					else: return 'False'
				elif obj[10]<=3:
					return 'False'
				else: return 'False'
			elif obj[11]>6:
				return 'True'
			else: return 'True'
		elif obj[13]>1.0:
			# {"feature": "Passanger", "instances": 27, "metric_value": 0.6052, "depth": 3}
			if obj[0]>0:
				# {"feature": "Income", "instances": 26, "metric_value": 0.5159, "depth": 4}
				if obj[11]<=4:
					return 'True'
				elif obj[11]>4:
					# {"feature": "Restaurantlessthan20", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[14]<=2.0:
						return 'True'
					elif obj[14]>2.0:
						# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[2]>1:
							# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[2]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]<=1:
		# {"feature": "Education", "instances": 23, "metric_value": 0.8281, "depth": 2}
		if obj[9]>1:
			return 'False'
		elif obj[9]<=1:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[10]>2:
				# {"feature": "Distance", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[17]<=2:
					return 'True'
				elif obj[17]>2:
					return 'False'
				else: return 'False'
			elif obj[10]<=2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
