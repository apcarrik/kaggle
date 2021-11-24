def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[2]<=2:
		# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.9923, "depth": 2}
		if obj[15]<=2.0:
			# {"feature": "Restaurantlessthan20", "instances": 27, "metric_value": 0.999, "depth": 3}
			if obj[14]>1.0:
				# {"feature": "Education", "instances": 22, "metric_value": 0.994, "depth": 4}
				if obj[9]<=2:
					# {"feature": "Occupation", "instances": 20, "metric_value": 1.0, "depth": 5}
					if obj[10]>2:
						# {"feature": "Income", "instances": 17, "metric_value": 0.9774, "depth": 6}
						if obj[11]<=7:
							# {"feature": "Age", "instances": 15, "metric_value": 0.9968, "depth": 7}
							if obj[6]>2:
								# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[3]>0:
									# {"feature": "Coupon_validity", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[4]<=0:
										return 'True'
									elif obj[4]>0:
										# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7]>0:
											return 'True'
										elif obj[7]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[3]<=0:
									return 'False'
								else: return 'False'
							elif obj[6]<=2:
								# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[3]>0:
									return 'False'
								elif obj[3]<=0:
									# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[1]<=0:
										return 'True'
									elif obj[1]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						elif obj[11]>7:
							return 'False'
						else: return 'False'
					elif obj[10]<=2:
						return 'True'
					else: return 'True'
				elif obj[9]>2:
					return 'False'
				else: return 'False'
			elif obj[14]<=1.0:
				# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[1]<=0:
					return 'True'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[15]>2.0:
			return 'True'
		else: return 'True'
	elif obj[2]>2:
		return 'True'
	else: return 'True'
