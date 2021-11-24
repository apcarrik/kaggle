def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Income", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[13]<=6:
		# {"feature": "Age", "instances": 30, "metric_value": 0.971, "depth": 2}
		if obj[8]<=6:
			# {"feature": "Coupon", "instances": 27, "metric_value": 0.9183, "depth": 3}
			if obj[5]<=3:
				# {"feature": "Passanger", "instances": 19, "metric_value": 0.998, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Bar", "instances": 16, "metric_value": 0.9544, "depth": 5}
					if obj[14]<=2.0:
						# {"feature": "Education", "instances": 14, "metric_value": 0.8631, "depth": 6}
						if obj[11]<=2:
							# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 7}
							if obj[12]>2:
								# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[6]<=0:
									# {"feature": "Driving_to", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[0]<=1:
										return 'False'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[12]<=2:
								return 'False'
							else: return 'False'
						elif obj[11]>2:
							return 'False'
						else: return 'False'
					elif obj[14]>2.0:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			elif obj[5]>3:
				return 'False'
			else: return 'False'
		elif obj[8]>6:
			return 'True'
		else: return 'True'
	elif obj[13]>6:
		return 'True'
	else: return 'True'
