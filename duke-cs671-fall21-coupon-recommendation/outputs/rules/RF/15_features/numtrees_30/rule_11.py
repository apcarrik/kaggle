def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Children", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[6]>0:
		# {"feature": "Bar", "instances": 17, "metric_value": 0.9774, "depth": 2}
		if obj[10]<=1.0:
			# {"feature": "Time", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[1]>0:
				# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[12]<=1.0:
					return 'False'
				elif obj[12]>1.0:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[10]>1.0:
			return 'False'
		else: return 'False'
	elif obj[6]<=0:
		# {"feature": "Age", "instances": 17, "metric_value": 0.3228, "depth": 2}
		if obj[5]>0:
			return 'True'
		elif obj[5]<=0:
			# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=1:
				return 'True'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
