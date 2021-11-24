def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[9]<=2:
		# {"feature": "Occupation", "instances": 26, "metric_value": 0.9306, "depth": 2}
		if obj[10]<=11:
			# {"feature": "Restaurantlessthan20", "instances": 22, "metric_value": 0.976, "depth": 3}
			if obj[14]<=3.0:
				# {"feature": "Income", "instances": 20, "metric_value": 0.9341, "depth": 4}
				if obj[11]>3:
					# {"feature": "Coupon", "instances": 16, "metric_value": 0.9887, "depth": 5}
					if obj[3]<=3:
						# {"feature": "Time", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[2]>1:
							# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[12]<=0.0:
									return 'False'
								elif obj[12]>0.0:
									return 'True'
								else: return 'True'
							elif obj[0]>2:
								return 'True'
							else: return 'True'
						elif obj[2]<=1:
							return 'True'
						else: return 'True'
					elif obj[3]>3:
						# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[1]<=0:
							return 'False'
						elif obj[1]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[11]<=3:
					return 'True'
				else: return 'True'
			elif obj[14]>3.0:
				return 'False'
			else: return 'False'
		elif obj[10]>11:
			return 'True'
		else: return 'True'
	elif obj[9]>2:
		# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 2}
		if obj[3]>3:
			return 'False'
		elif obj[3]<=3:
			# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[0]>0:
				# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[7]<=1:
					return 'True'
				elif obj[7]>1:
					return 'False'
				else: return 'False'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
