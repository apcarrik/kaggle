def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Weather", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[1]<=0:
		# {"feature": "Occupation", "instances": 28, "metric_value": 0.9059, "depth": 2}
		if obj[11]>2:
			# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 3}
			if obj[4]>0:
				# {"feature": "Temperature", "instances": 21, "metric_value": 0.9183, "depth": 4}
				if obj[2]>30:
					# {"feature": "Maritalstatus", "instances": 18, "metric_value": 0.9641, "depth": 5}
					if obj[8]<=2:
						# {"feature": "Time", "instances": 16, "metric_value": 0.896, "depth": 6}
						if obj[3]<=2:
							# {"feature": "Bar", "instances": 12, "metric_value": 0.9799, "depth": 7}
							if obj[13]<=1.0:
								# {"feature": "Age", "instances": 10, "metric_value": 0.8813, "depth": 8}
								if obj[7]<=3:
									# {"feature": "Income", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[12]>1:
										# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[14]<=1.0:
											return 'True'
										elif obj[14]>1.0:
											return 'False'
										else: return 'False'
									elif obj[12]<=1:
										return 'False'
									else: return 'False'
								elif obj[7]>3:
									return 'True'
								else: return 'True'
							elif obj[13]>1.0:
								return 'False'
							else: return 'False'
						elif obj[3]>2:
							return 'True'
						else: return 'True'
					elif obj[8]>2:
						return 'False'
					else: return 'False'
				elif obj[2]<=30:
					return 'True'
				else: return 'True'
			elif obj[4]<=0:
				return 'False'
			else: return 'False'
		elif obj[11]<=2:
			return 'True'
		else: return 'True'
	elif obj[1]>0:
		# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[11]>1:
			return 'False'
		elif obj[11]<=1:
			# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]<=30:
				return 'False'
			elif obj[2]>30:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
