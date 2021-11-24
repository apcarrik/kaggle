def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coupon_validity", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[5]<=0:
		# {"feature": "Bar", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[13]<=0.0:
			# {"feature": "Income", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[12]>1:
				# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[12]<=1:
				return 'False'
			else: return 'False'
		elif obj[13]>0.0:
			return 'True'
		else: return 'True'
	elif obj[5]>0:
		# {"feature": "Passanger", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[0]<=2:
			return 'False'
		elif obj[0]>2:
			# {"feature": "Maritalstatus", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[8]>0:
				return 'True'
			elif obj[8]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
