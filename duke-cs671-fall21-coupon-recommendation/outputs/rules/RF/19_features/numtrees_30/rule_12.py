def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[16]>0.0:
		# {"feature": "Coupon_validity", "instances": 28, "metric_value": 0.8113, "depth": 2}
		if obj[5]>0:
			# {"feature": "Passanger", "instances": 14, "metric_value": 1.0, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Weather", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[1]<=0:
					# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[4]>2:
						# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[12]<=5:
							return 'True'
						elif obj[12]>5:
							return 'False'
						else: return 'False'
					elif obj[4]<=2:
						return 'False'
					else: return 'False'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[5]<=0:
			return 'True'
		else: return 'True'
	elif obj[16]<=0.0:
		# {"feature": "Weather", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[1]<=0:
			return 'False'
		elif obj[1]>0:
			return 'True'
		else: return 'True'
	else: return 'False'
