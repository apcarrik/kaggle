def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[2]<=1:
		# {"feature": "Distance", "instances": 14, "metric_value": 0.9403, "depth": 2}
		if obj[15]<=2:
			# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[13]<=1.0:
				return 'False'
			elif obj[13]>1.0:
				# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[15]>2:
			return 'True'
		else: return 'True'
	elif obj[2]>1:
		return 'True'
	else: return 'True'
