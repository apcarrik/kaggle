def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[13]>1:
		# {"feature": "Income", "instances": 15, "metric_value": 0.9183, "depth": 2}
		if obj[8]>1:
			# {"feature": "Occupation", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[7]>6:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			elif obj[7]<=6:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[5]>0:
						return 'True'
					elif obj[5]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[8]<=1:
			return 'False'
		else: return 'False'
	elif obj[13]<=1:
		return 'True'
	else: return 'True'
