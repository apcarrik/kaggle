def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 8148, "metric_value": 0.9876, "depth": 1}
	if obj[1]>1:
		# {"feature": "Passanger", "instances": 5867, "metric_value": 0.9568, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Distance", "instances": 3640, "metric_value": 0.982, "depth": 3}
			if obj[5]<=1:
				# {"feature": "Restaurant20to50", "instances": 1967, "metric_value": 0.9259, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Education", "instances": 1583, "metric_value": 0.9134, "depth": 5}
					if obj[2]>1:
						# {"feature": "Occupation", "instances": 897, "metric_value": 0.9331, "depth": 6}
						if obj[3]<=13.342102194302225:
							return 'True'
						elif obj[3]>13.342102194302225:
							return 'True'
						else: return 'True'
					elif obj[2]<=1:
						# {"feature": "Occupation", "instances": 686, "metric_value": 0.8834, "depth": 6}
						if obj[3]<=20.403723888741776:
							return 'True'
						elif obj[3]>20.403723888741776:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					# {"feature": "Occupation", "instances": 384, "metric_value": 0.9669, "depth": 5}
					if obj[3]<=13:
						# {"feature": "Education", "instances": 354, "metric_value": 0.959, "depth": 6}
						if obj[2]<=2:
							return 'True'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					elif obj[3]>13:
						# {"feature": "Education", "instances": 30, "metric_value": 0.9968, "depth": 6}
						if obj[2]>2:
							return 'False'
						elif obj[2]<=2:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[5]>1:
				# {"feature": "Education", "instances": 1673, "metric_value": 0.9993, "depth": 4}
				if obj[2]>0:
					# {"feature": "Occupation", "instances": 1105, "metric_value": 0.9955, "depth": 5}
					if obj[3]<=19.43193856008163:
						# {"feature": "Restaurant20to50", "instances": 1029, "metric_value": 0.9969, "depth": 6}
						if obj[4]>-1.0:
							return 'False'
						elif obj[4]<=-1.0:
							return 'False'
						else: return 'False'
					elif obj[3]>19.43193856008163:
						# {"feature": "Restaurant20to50", "instances": 76, "metric_value": 0.9495, "depth": 6}
						if obj[4]<=1.0:
							return 'False'
						elif obj[4]>1.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]<=0:
					# {"feature": "Restaurant20to50", "instances": 568, "metric_value": 0.9971, "depth": 5}
					if obj[4]<=2.0:
						# {"feature": "Occupation", "instances": 532, "metric_value": 0.9993, "depth": 6}
						if obj[3]>1.6714468218684795:
							return 'True'
						elif obj[3]<=1.6714468218684795:
							return 'False'
						else: return 'False'
					elif obj[4]>2.0:
						# {"feature": "Occupation", "instances": 36, "metric_value": 0.7642, "depth": 6}
						if obj[3]>1:
							return 'True'
						elif obj[3]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]>1:
			# {"feature": "Education", "instances": 2227, "metric_value": 0.8909, "depth": 3}
			if obj[2]>0:
				# {"feature": "Occupation", "instances": 1463, "metric_value": 0.9057, "depth": 4}
				if obj[3]<=19.11385554190759:
					# {"feature": "Restaurant20to50", "instances": 1386, "metric_value": 0.8992, "depth": 5}
					if obj[4]<=2.0:
						# {"feature": "Distance", "instances": 1265, "metric_value": 0.893, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[4]>2.0:
						# {"feature": "Distance", "instances": 121, "metric_value": 0.9521, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]>19.11385554190759:
					# {"feature": "Restaurant20to50", "instances": 77, "metric_value": 0.9852, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Distance", "instances": 56, "metric_value": 0.9241, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						# {"feature": "Distance", "instances": 21, "metric_value": 0.9183, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Restaurant20to50", "instances": 764, "metric_value": 0.8591, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Occupation", "instances": 562, "metric_value": 0.8886, "depth": 5}
					if obj[3]<=18.63348904995262:
						# {"feature": "Distance", "instances": 520, "metric_value": 0.9014, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[3]>18.63348904995262:
						# {"feature": "Distance", "instances": 42, "metric_value": 0.65, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>1.0:
					# {"feature": "Occupation", "instances": 202, "metric_value": 0.7562, "depth": 5}
					if obj[3]<=18:
						# {"feature": "Distance", "instances": 196, "metric_value": 0.7683, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[3]>18:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[1]<=1:
		# {"feature": "Restaurant20to50", "instances": 2281, "metric_value": 0.9817, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Occupation", "instances": 1500, "metric_value": 0.9481, "depth": 3}
			if obj[3]>1.9904707123952177:
				# {"feature": "Passanger", "instances": 1255, "metric_value": 0.9646, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Education", "instances": 1087, "metric_value": 0.9533, "depth": 5}
					if obj[2]>0:
						# {"feature": "Distance", "instances": 730, "metric_value": 0.9284, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[2]<=0:
						# {"feature": "Distance", "instances": 357, "metric_value": 0.9875, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Education", "instances": 168, "metric_value": 0.9999, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Distance", "instances": 140, "metric_value": 0.9987, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[2]>2:
						# {"feature": "Distance", "instances": 28, "metric_value": 0.9852, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[3]<=1.9904707123952177:
				# {"feature": "Education", "instances": 245, "metric_value": 0.8097, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Passanger", "instances": 225, "metric_value": 0.7722, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Distance", "instances": 189, "metric_value": 0.7344, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[0]>2:
						# {"feature": "Distance", "instances": 36, "metric_value": 0.9183, "depth": 6}
						if obj[5]>1:
							return 'False'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]>3:
					# {"feature": "Passanger", "instances": 20, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						# {"feature": "Distance", "instances": 19, "metric_value": 0.998, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]>1.0:
			# {"feature": "Distance", "instances": 781, "metric_value": 0.9984, "depth": 3}
			if obj[5]<=2:
				# {"feature": "Education", "instances": 641, "metric_value": 0.9939, "depth": 4}
				if obj[2]>0:
					# {"feature": "Occupation", "instances": 442, "metric_value": 0.9993, "depth": 5}
					if obj[3]<=19.17084245775628:
						# {"feature": "Passanger", "instances": 415, "metric_value": 0.9985, "depth": 6}
						if obj[0]>0:
							return 'True'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[3]>19.17084245775628:
						# {"feature": "Passanger", "instances": 27, "metric_value": 0.9751, "depth": 6}
						if obj[0]<=2:
							return 'False'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]<=0:
					# {"feature": "Occupation", "instances": 199, "metric_value": 0.9628, "depth": 5}
					if obj[3]<=9:
						# {"feature": "Passanger", "instances": 132, "metric_value": 0.9919, "depth": 6}
						if obj[0]<=2:
							return 'True'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					elif obj[3]>9:
						# {"feature": "Passanger", "instances": 67, "metric_value": 0.8395, "depth": 6}
						if obj[0]<=2:
							return 'True'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[5]>2:
				# {"feature": "Passanger", "instances": 140, "metric_value": 0.9821, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Occupation", "instances": 139, "metric_value": 0.9802, "depth": 5}
					if obj[3]>0:
						# {"feature": "Education", "instances": 138, "metric_value": 0.9781, "depth": 6}
						if obj[2]<=2:
							return 'False'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	else: return 'False'
