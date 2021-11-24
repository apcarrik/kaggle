def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Passanger", "instances": 41, "metric_value": 0.9474, "depth": 1}
	if obj[1]>0:
		# {"feature": "Weather", "instances": 38, "metric_value": 0.8997, "depth": 2}
		if obj[2]<=1:
			# {"feature": "Carryaway", "instances": 35, "metric_value": 0.8224, "depth": 3}
			if obj[16]>1.0:
				# {"feature": "Restaurantlessthan20", "instances": 33, "metric_value": 0.7455, "depth": 4}
				if obj[17]<=3.0:
					# {"feature": "Education", "instances": 31, "metric_value": 0.6374, "depth": 5}
					if obj[11]>0:
						return 'True'
					elif obj[11]<=0:
						# {"feature": "Direction_same", "instances": 14, "metric_value": 0.9403, "depth": 6}
						if obj[19]<=0:
							# {"feature": "Time", "instances": 10, "metric_value": 1.0, "depth": 7}
							if obj[4]<=3:
								# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[5]<=3:
									# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[3]>55:
										# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=5:
											return 'False'
										elif obj[8]>5:
											return 'True'
										else: return 'True'
									elif obj[3]<=55:
										return 'True'
									else: return 'True'
								elif obj[5]>3:
									return 'False'
								else: return 'False'
							elif obj[4]>3:
								return 'True'
							else: return 'True'
						elif obj[19]>0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[17]>3.0:
					return 'False'
				else: return 'False'
			elif obj[16]<=1.0:
				return 'False'
			else: return 'False'
		elif obj[2]>1:
			return 'False'
		else: return 'False'
	elif obj[1]<=0:
		return 'False'
	else: return 'False'
