def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[3]>1:
		# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[13]>0.0:
			# {"feature": "Income", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[11]>1:
				return 'True'
			elif obj[11]<=1:
				# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[13]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[3]<=1:
		return 'False'
	else: return 'False'
