def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Income", "instances": 15, "metric_value": 0.9183, "depth": 2}
		if obj[10]>0:
			# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[12]<=2.0:
				return 'False'
			elif obj[12]>2.0:
				return 'True'
			else: return 'True'
		elif obj[10]<=0:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		return 'True'
	else: return 'True'
