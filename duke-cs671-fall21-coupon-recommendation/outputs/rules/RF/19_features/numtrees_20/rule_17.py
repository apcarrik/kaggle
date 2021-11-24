def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[16]>0.0:
		# {"feature": "Restaurantlessthan20", "instances": 45, "metric_value": 0.9996, "depth": 2}
		if obj[15]>1.0:
			# {"feature": "Age", "instances": 37, "metric_value": 0.974, "depth": 3}
			if obj[7]<=3:
				# {"feature": "Income", "instances": 25, "metric_value": 0.9988, "depth": 4}
				if obj[12]>1:
					# {"feature": "Time", "instances": 16, "metric_value": 0.896, "depth": 5}
					if obj[3]>0:
						# {"feature": "Children", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[9]>0:
							# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[4]>0:
								return 'False'
							elif obj[4]<=0:
								# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2]<=55:
									return 'True'
								elif obj[2]>55:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[9]<=0:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				elif obj[12]<=1:
					# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[10]<=2:
						return 'True'
					elif obj[10]>2:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[7]>3:
				# {"feature": "Occupation", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[11]<=7:
					return 'True'
				elif obj[11]>7:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4]>1:
						# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[8]>0:
							return 'False'
						elif obj[8]<=0:
							return 'True'
						else: return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[15]<=1.0:
			# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[10]<=2:
				return 'False'
			elif obj[10]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[16]<=0.0:
		return 'True'
	else: return 'True'
