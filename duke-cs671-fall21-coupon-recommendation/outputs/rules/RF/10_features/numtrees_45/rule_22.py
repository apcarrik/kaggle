def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[4]<=10:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.7642, "depth": 2}
		if obj[2]>2:
			return 'True'
		elif obj[2]<=2:
			# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[3]>1:
				# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=0.0:
					return 'False'
				elif obj[5]>0.0:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[4]>10:
		return 'False'
	else: return 'False'
