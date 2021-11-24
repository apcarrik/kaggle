def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Age", "instances": 16, "metric_value": 0.8113, "depth": 2}
		if obj[4]>0:
			# {"feature": "Time", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[8]<=1.0:
					return 'True'
				elif obj[8]>1.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]<=0:
			return 'False'
		else: return 'False'
	elif obj[2]>3:
		# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[4]<=4:
			return 'False'
		elif obj[4]>4:
			return 'True'
		else: return 'True'
	else: return 'False'
