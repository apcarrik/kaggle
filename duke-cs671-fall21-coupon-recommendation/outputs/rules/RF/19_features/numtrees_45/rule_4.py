def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Gender", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[6]<=0:
		# {"feature": "Weather", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[1]<=0:
			# {"feature": "Age", "instances": 14, "metric_value": 0.7496, "depth": 3}
			if obj[7]>1:
				return 'True'
			elif obj[7]<=1:
				# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[14]<=2.0:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4]>0:
						return 'True'
					elif obj[4]<=0:
						return 'False'
					else: return 'False'
				elif obj[14]>2.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]>0:
			return 'False'
		else: return 'False'
	elif obj[6]>0:
		# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[7]>2:
			return 'False'
		elif obj[7]<=2:
			# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]<=30:
				return 'False'
			elif obj[2]>30:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
