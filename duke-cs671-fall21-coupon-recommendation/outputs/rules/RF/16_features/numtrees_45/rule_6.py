def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[15]>1:
		# {"feature": "Education", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[8]<=2:
			# {"feature": "Gender", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[5]<=0:
				return 'False'
			elif obj[5]>0:
				# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[2]<=1:
					return 'False'
				elif obj[2]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[8]>2:
			# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[7]<=0:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]>0:
					return 'False'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			elif obj[7]>0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[15]<=1:
		# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 2}
		if obj[13]<=1.0:
			return 'True'
		elif obj[13]>1.0:
			return 'False'
		else: return 'False'
	else: return 'True'
