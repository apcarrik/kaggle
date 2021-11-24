def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Weather", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[2]<=1:
		# {"feature": "Passanger", "instances": 31, "metric_value": 0.9072, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 29, "metric_value": 0.8498, "depth": 3}
			if obj[12]<=12:
				# {"feature": "Restaurantlessthan20", "instances": 24, "metric_value": 0.9183, "depth": 4}
				if obj[16]>1.0:
					# {"feature": "Income", "instances": 20, "metric_value": 0.8113, "depth": 5}
					if obj[13]>3:
						# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[17]<=2.0:
							return 'True'
						elif obj[17]>2.0:
							return 'False'
						else: return 'False'
					elif obj[13]<=3:
						# {"feature": "Driving_to", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[4]>2:
								return 'True'
							elif obj[4]<=2:
								# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[3]<=55:
									# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[5]>0:
										return 'True'
									elif obj[5]<=0:
										return 'False'
									else: return 'False'
								elif obj[3]>55:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[16]<=1.0:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[11]<=3:
						return 'False'
					elif obj[11]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[12]>12:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	elif obj[2]>1:
		return 'False'
	else: return 'False'
