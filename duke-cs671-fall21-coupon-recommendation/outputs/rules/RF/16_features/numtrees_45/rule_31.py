def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[11]<=2.0:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[9]<=7:
			# {"feature": "Age", "instances": 12, "metric_value": 1.0, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Income", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[10]<=4:
					return 'True'
				elif obj[10]>4:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=1:
						return 'False'
					elif obj[2]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[6]>2:
				return 'False'
			else: return 'False'
		elif obj[9]>7:
			return 'True'
		else: return 'True'
	elif obj[11]>2.0:
		# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[9]>1:
			return 'False'
		elif obj[9]<=1:
			return 'True'
		else: return 'True'
	else: return 'False'
