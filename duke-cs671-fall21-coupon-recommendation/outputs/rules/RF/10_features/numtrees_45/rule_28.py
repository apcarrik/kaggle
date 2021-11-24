def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.9774, "depth": 2}
		if obj[7]>0.0:
			# {"feature": "Bar", "instances": 14, "metric_value": 1.0, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[4]>2:
					# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]<=2:
							return 'True'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]<=2:
					# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]>2.0:
				return 'False'
			else: return 'False'
		elif obj[7]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
