def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Weather", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[1]<=0:
		# {"feature": "Bar", "instances": 28, "metric_value": 0.9963, "depth": 2}
		if obj[13]<=2.0:
			# {"feature": "Time", "instances": 24, "metric_value": 0.9544, "depth": 3}
			if obj[3]<=3:
				# {"feature": "Age", "instances": 17, "metric_value": 0.9975, "depth": 4}
				if obj[7]>0:
					# {"feature": "Coupon", "instances": 14, "metric_value": 0.9403, "depth": 5}
					if obj[4]>1:
						# {"feature": "Income", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[12]<=2:
							# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[14]>-1.0:
								return 'True'
							elif obj[14]<=-1.0:
								return 'False'
							else: return 'False'
						elif obj[12]>2:
							return 'False'
						else: return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[7]<=0:
					return 'True'
				else: return 'True'
			elif obj[3]>3:
				return 'True'
			else: return 'True'
		elif obj[13]>2.0:
			return 'False'
		else: return 'False'
	elif obj[1]>0:
		return 'False'
	else: return 'False'
