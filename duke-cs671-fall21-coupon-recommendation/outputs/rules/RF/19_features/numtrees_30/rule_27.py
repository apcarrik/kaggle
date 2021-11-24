def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[10]<=3:
		# {"feature": "Coffeehouse", "instances": 32, "metric_value": 0.9745, "depth": 2}
		if obj[14]<=3.0:
			# {"feature": "Temperature", "instances": 29, "metric_value": 0.9923, "depth": 3}
			if obj[2]<=55:
				# {"feature": "Weather", "instances": 18, "metric_value": 0.9911, "depth": 4}
				if obj[1]>0:
					# {"feature": "Age", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[7]>2:
						# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[3]<=2:
							# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[12]<=4:
								# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0]<=1:
									return 'False'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							elif obj[12]>4:
								return 'True'
							else: return 'True'
						elif obj[3]>2:
							return 'False'
						else: return 'False'
					elif obj[7]<=2:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[4]<=3:
						return 'True'
					elif obj[4]>3:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=2:
							return 'True'
						elif obj[0]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[2]>55:
				# {"feature": "Age", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[7]<=4:
					# {"feature": "Income", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[12]<=7:
						return 'False'
					elif obj[12]>7:
						return 'True'
					else: return 'True'
				elif obj[7]>4:
					# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[12]<=4:
						return 'True'
					elif obj[12]>4:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[14]>3.0:
			return 'False'
		else: return 'False'
	elif obj[10]>3:
		return 'True'
	else: return 'True'
