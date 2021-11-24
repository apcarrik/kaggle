def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Children", "instances": 23, "metric_value": 0.6666, "depth": 1}
	if obj[8]<=0:
		return 'True'
	elif obj[8]>0:
		# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 2}
		if obj[9]<=0:
			# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[10]>1:
				return 'False'
			elif obj[10]<=1:
				return 'True'
			else: return 'True'
		elif obj[9]>0:
			return 'True'
		else: return 'True'
	else: return 'True'
