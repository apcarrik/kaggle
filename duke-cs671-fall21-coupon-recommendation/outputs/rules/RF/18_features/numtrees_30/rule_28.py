def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[3]>1:
		# {"feature": "Bar", "instances": 26, "metric_value": 0.7793, "depth": 2}
		if obj[12]<=1.0:
			# {"feature": "Restaurantlessthan20", "instances": 19, "metric_value": 0.4855, "depth": 3}
			if obj[14]<=3.0:
				# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.3095, "depth": 4}
				if obj[15]<=1.0:
					return 'True'
				elif obj[15]>1.0:
					# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[6]<=6:
						return 'True'
					elif obj[6]>6:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[14]>3.0:
				return 'False'
			else: return 'False'
		elif obj[12]>1.0:
			# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[9]>0:
				return 'False'
			elif obj[9]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]<=1:
		# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 2}
		if obj[10]<=9:
			return 'False'
		elif obj[10]>9:
			# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[8]<=0:
				return 'False'
			elif obj[8]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
