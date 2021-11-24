def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[11]<=2.0:
		# {"feature": "Passanger", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[6]<=2:
				return 'False'
			elif obj[6]>2:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>1:
					return 'False'
				elif obj[1]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]>1:
			# {"feature": "Age", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[4]>2:
				# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[10]<=3.0:
					return 'True'
				elif obj[10]>3.0:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[11]>2.0:
		return 'True'
	else: return 'True'
