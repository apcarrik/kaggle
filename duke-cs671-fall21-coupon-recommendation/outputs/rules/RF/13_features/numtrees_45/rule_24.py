def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.9774, "depth": 2}
		if obj[9]<=2.0:
			# {"feature": "Direction_same", "instances": 14, "metric_value": 1.0, "depth": 3}
			if obj[11]<=0:
				# {"feature": "Children", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[7]<=7:
						# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]>0:
							return 'True'
						elif obj[4]<=0:
							return 'False'
						else: return 'False'
					elif obj[7]>7:
						return 'False'
					else: return 'False'
				elif obj[5]>0:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]>1:
							return 'True'
						elif obj[1]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[11]>0:
				return 'False'
			else: return 'False'
		elif obj[9]>2.0:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		return 'False'
	else: return 'False'
