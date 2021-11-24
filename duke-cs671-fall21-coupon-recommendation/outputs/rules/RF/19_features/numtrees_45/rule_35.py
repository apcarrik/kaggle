def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[14]>0.0:
		# {"feature": "Bar", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[13]<=1.0:
			# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[10]<=2:
				return 'True'
			elif obj[10]>2:
				# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[16]>0.0:
					return 'False'
				elif obj[16]<=0.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[13]>1.0:
			# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[7]<=4:
				return 'False'
			elif obj[7]>4:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[14]<=0.0:
		return 'True'
	else: return 'True'
