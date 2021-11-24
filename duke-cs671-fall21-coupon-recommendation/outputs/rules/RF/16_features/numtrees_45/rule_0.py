def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[10]<=6:
		# {"feature": "Education", "instances": 16, "metric_value": 0.9887, "depth": 2}
		if obj[8]<=2:
			# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[12]>1.0:
				return 'True'
			elif obj[12]<=1.0:
				# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[14]<=0:
					return 'False'
				elif obj[14]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[8]>2:
			# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[15]>1:
				return 'False'
			elif obj[15]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[10]>6:
		return 'True'
	else: return 'True'
