def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Income", "instances": 85, "metric_value": 0.971, "depth": 1}
	if obj[11]>0:
		# {"feature": "Restaurant20to50", "instances": 79, "metric_value": 0.986, "depth": 2}
		if obj[15]<=1.0:
			# {"feature": "Time", "instances": 53, "metric_value": 0.9977, "depth": 3}
			if obj[2]>1:
				# {"feature": "Coupon", "instances": 30, "metric_value": 0.971, "depth": 4}
				if obj[3]>1:
					# {"feature": "Education", "instances": 17, "metric_value": 0.6723, "depth": 5}
					if obj[9]>1:
						# {"feature": "Restaurantlessthan20", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[14]>1.0:
							# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[0]>2:
								# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[5]<=0:
									return 'True'
								elif obj[5]>0:
									return 'False'
								else: return 'False'
							elif obj[0]<=2:
								return 'False'
							else: return 'False'
						elif obj[14]<=1.0:
							return 'True'
						else: return 'True'
					elif obj[9]<=1:
						return 'True'
					else: return 'True'
				elif obj[3]<=1:
					# {"feature": "Children", "instances": 13, "metric_value": 0.8905, "depth": 5}
					if obj[8]<=0:
						# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[9]<=3:
							return 'False'
						elif obj[9]>3:
							return 'True'
						else: return 'True'
					elif obj[8]>0:
						# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[5]<=0:
							return 'True'
						elif obj[5]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=1:
				# {"feature": "Education", "instances": 23, "metric_value": 0.8865, "depth": 4}
				if obj[9]>0:
					# {"feature": "Age", "instances": 17, "metric_value": 0.9774, "depth": 5}
					if obj[6]<=4:
						# {"feature": "Children", "instances": 14, "metric_value": 1.0, "depth": 6}
						if obj[8]<=0:
							# {"feature": "Coupon_validity", "instances": 12, "metric_value": 0.9799, "depth": 7}
							if obj[4]<=0:
								# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[10]<=20:
									# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[13]<=2.0:
										return 'True'
									elif obj[13]>2.0:
										return 'False'
									else: return 'False'
								elif obj[10]>20:
									return 'False'
								else: return 'False'
							elif obj[4]>0:
								return 'False'
							else: return 'False'
						elif obj[8]>0:
							return 'True'
						else: return 'True'
					elif obj[6]>4:
						return 'False'
					else: return 'False'
				elif obj[9]<=0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[15]>1.0:
			# {"feature": "Education", "instances": 26, "metric_value": 0.7793, "depth": 3}
			if obj[9]<=2:
				# {"feature": "Occupation", "instances": 19, "metric_value": 0.2975, "depth": 4}
				if obj[10]<=20:
					return 'True'
				elif obj[10]>20:
					return 'False'
				else: return 'False'
			elif obj[9]>2:
				# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[5]>0:
					return 'False'
				elif obj[5]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[11]<=0:
		return 'True'
	else: return 'True'
