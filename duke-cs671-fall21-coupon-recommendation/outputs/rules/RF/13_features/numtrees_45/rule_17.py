def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Education", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[6]>0:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[7]<=10:
					# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[8]<=0.0:
						# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[9]<=1.0:
								return 'True'
							elif obj[9]>1.0:
								return 'False'
							else: return 'False'
						elif obj[1]>1:
							return 'False'
						else: return 'False'
					elif obj[8]>0.0:
						return 'True'
					else: return 'True'
				elif obj[7]>10:
					return 'False'
				else: return 'False'
			elif obj[6]<=0:
				return 'False'
			else: return 'False'
		elif obj[2]>3:
			return 'False'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[9]>0.0:
			return 'True'
		elif obj[9]<=0.0:
			return 'False'
		else: return 'False'
	else: return 'True'
