def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 12, "metric_value": 0.9183, "depth": 2}
		if obj[9]>1:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[10]>6:
				# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]<=0:
					return 'True'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			elif obj[10]<=6:
				return 'False'
			else: return 'False'
		elif obj[9]<=1:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Distance", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[16]>1:
			return 'False'
		elif obj[16]<=1:
			# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=0:
				return 'True'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
