def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]<=1:
		# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[3]>3:
			return 'False'
		elif obj[3]<=3:
			# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[10]<=8:
				# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[13]<=2.0:
					return 'True'
				elif obj[13]>2.0:
					return 'False'
				else: return 'False'
			elif obj[10]>8:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]>1:
		# {"feature": "Occupation", "instances": 11, "metric_value": 0.8454, "depth": 2}
		if obj[10]>5:
			# {"feature": "Maritalstatus", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[7]>0:
				# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[6]>1:
					return 'True'
				elif obj[6]<=1:
					return 'False'
				else: return 'False'
			elif obj[7]<=0:
				return 'False'
			else: return 'False'
		elif obj[10]<=5:
			return 'True'
		else: return 'True'
	else: return 'True'
