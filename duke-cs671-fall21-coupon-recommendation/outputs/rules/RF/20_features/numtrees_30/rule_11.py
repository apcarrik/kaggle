def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[12]>3:
		# {"feature": "Coupon", "instances": 25, "metric_value": 0.9427, "depth": 2}
		if obj[5]>0:
			# {"feature": "Weather", "instances": 22, "metric_value": 0.8454, "depth": 3}
			if obj[2]<=1:
				# {"feature": "Bar", "instances": 20, "metric_value": 0.7219, "depth": 4}
				if obj[14]<=2.0:
					# {"feature": "Age", "instances": 19, "metric_value": 0.6292, "depth": 5}
					if obj[8]<=3:
						# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[15]>0.0:
							# {"feature": "Income", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[13]>0:
								return 'True'
							elif obj[13]<=0:
								# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]>2:
									return 'True'
								elif obj[1]<=2:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[15]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[8]>3:
						return 'True'
					else: return 'True'
				elif obj[14]>2.0:
					return 'False'
				else: return 'False'
			elif obj[2]>1:
				return 'False'
			else: return 'False'
		elif obj[5]<=0:
			return 'False'
		else: return 'False'
	elif obj[12]<=3:
		return 'False'
	else: return 'False'
