def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.6723, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[6]<=5:
				# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[8]<=0.0:
						return 'False'
					elif obj[8]>0.0:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			elif obj[6]>5:
				return 'False'
			else: return 'False'
		elif obj[2]>3:
			return 'False'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[9]<=2.0:
			return 'True'
		elif obj[9]>2.0:
			return 'False'
		else: return 'False'
	else: return 'True'
