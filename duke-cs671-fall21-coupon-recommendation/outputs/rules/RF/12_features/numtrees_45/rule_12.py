def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.9852, "depth": 2}
		if obj[6]<=8:
			# {"feature": "Time", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=0:
					return 'False'
				elif obj[2]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]>8:
			return 'False'
		else: return 'False'
	elif obj[0]>1:
		return 'True'
	else: return 'True'
